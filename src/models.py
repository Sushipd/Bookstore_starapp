from sqlalchemy import create_engine
from sqlalchemy.sql import text
import os

class Models:
    def __init__(self):
        self.engine = create_engine(os.environ.get('DB_URL', 'postgresql://hieu:hieu@localhost:5432/bt5110'))

    def executeRawSql(self, statement, params={}):
        out = None
        with self.engine.connect() as con:
            out = con.execute(text(statement), params)
        return out

    def addUsers(self, value):
        return self.executeRawSql("""INSERT INTO manager(email, password) VALUES(:email, :password);""", value)

    def addBook(self, value):
        return self.executeRawSql("""INSERT INTO book(book_key, Printshop , Writer, Publication_date, Type, Book_name, Price) VALUES(:book_key, :Printshop , :Writer, :Publication_date, :Type, :Book_name, :Price);""", value)

    def addClerk(self, value):
        return self.executeRawSql("""INSERT INTO clerk(clerk_id, first_name, last_name, gender, email, date_of_hire) VALUES(:clerk_id, :first_name, :last_name, :gender, :email, :date_of_hire);""", value)

    def addDate(self, value):
        return self.executeRawSql("""INSERT INTO Date(Date_Key, Date_Time, Day_of_Week, Calendar_Month, Calender_Year, Holiday, Weekday) VALUES(:Date_Key, :Date_Time, :Day_of_Week, :Calendar_Month, :Calender_Year, :Holiday, :Weekday);""", value)

    def addFreqShopper(self, value):
        return self.executeRawSql("""INSERT INTO freq_shopper(shopper_id, title, first_name, last_name, gender, date_of_birth, city, street_address, phone) VALUES(:shopper_id, :title, :first_name, :last_name, :gender, :date_of_birth, :city, :street_address, :phone);""", value)

    def addPromotions(self, value):
        return self.executeRawSql("""INSERT INTO promotions(promotion_key, promotion_name, price_reduction_type, promotion_media_type, promotion_cost, promotion_begin_date, promotion_end_date) VALUES(:promotion_key, :promotion_name, :price_reduction_type, :promotion_media_type, :promotion_cost, :promotion_begin_date, :promotion_end_date);""", value)

    def addStores(self, value):
        return self.executeRawSql("""INSERT INTO stores(store_key, store_name, store_street_address, store_city, store_country, store_manager, selling_square_footage, first_open_date) VALUES(:store_key, :store_name, :store_street_address, :store_city, :store_country, :store_manager, :selling_square_footage, :first_open_date);""", value)

    def addTransfer(self, value):
        return self.executeRawSql("""INSERT INTO transfer(POS_transfer_id, date_key, book_key, clerk_id, shopper_id, promotion_key, store_key) VALUES(:POS_transfer_id, :date_key, :book_key, :clerk_id, :shopper_id, :promotion_key, :store_key);""", value)

    def getTransfers(self):
        return self.executeRawSql("select t.pos_transfer_id, t.date_key, t.book_key, t.clerk_id, t.shopper_id, t.promotion_key, t.store_key, d.Date_Time, b.Book_name, p.promotion_name, s.store_name from transfer t, date d, book b, promotions p, stores s where t.date_key=d.Date_Key and t.book_key=b.book_key and t.promotion_key=p.promotion_key and t.store_key=s.store_key order by d.Date_Time desc,t.clerk_id,t.shopper_id LIMIT 30;").mappings().all()

    def deleteTransfer(self, value):
        return self.executeRawSql("DELETE FROM transfer where pos_transfer_id=:pos_transfer_id;", value)
    
    def getTransfer(self, value):
        values = self.executeRawSql("""SELECT * FROM transfer WHERE pos_transfer_id=:pos_transfer_id;""", value).mappings().all()
        if len(values) == 0:
            raise Exception("Transfer {} has not been assigned".format(value["pos_transfer_id"]))
        return values[0]

    def updateTransfer(self, value):
        return self.executeRawSql("""UPDATE transfer SET date_key=:date_key,book_key=:book_key,clerk_id=:clerk_id,shopper_id=:shopper_id,promotion_key=:promotion_key,store_key=:store_key WHERE pos_transfer_id=:pos_transfer_id;""", value)

    def getPromotionFeatures(self):
        return self.executeRawSql("select p.promotion_key, p.promotion_name, (1-p.price_reduction_type)*100 as discount, p.promotion_begin_date, p.promotion_cost, p.promotion_media_type, p.promotion_end_date, q.total_income, (q.total_income-p.promotion_cost) as net_profit from (select p.promotion_key, sum(b.price*p.price_reduction_type) as total_income from promotions p, transfer t, book b where p.promotion_key = t.promotion_key and t.book_key = b.book_key group by p.promotion_key) as q, promotions p where q.promotion_key = p.promotion_key and p.price_reduction_type<1 order by net_profit desc; ").mappings().all()

    def getBestSellersEachMonth(self, value):
        values = self.executeRawSql("""select t.book_key, count(*), b.printshop, b.writer, b.publication_date, b.type, b.book_name, b.price from transfer t, date d, book b where t.date_key = d.date_key and t.book_key = b.book_key and d.calendar_month=:calendar_month and d.calender_year=:calender_year group by t.book_key, b.printshop, b.writer, b.publication_date, b.type, b.book_name, b.price order by count(*) DESC, b.publication_date DESC limit 20;""", value).mappings().all()
        if len(values) == 0:
            raise Exception("We have no data for Month {} Year {}".format(value["calendar_month"], value["calender_year"]))
        return values

    def getBestClerksEachMonth(self, value):
        values = self.executeRawSql("""select c.first_name, c.last_name, c.gender, c.email,c.clerk_id, d.calendar_month, d.calender_year, sum(p.price_reduction_type*b.price) as sale_vol from transfer t, book b, promotions p, clerk c, date d where t.clerk_id=c.clerk_id and t.book_key = b.book_key and t.promotion_key=p.promotion_key and t.date_key = d.date_key and d.calendar_month=:calendar_month and d.calender_year=:calender_year group by c.clerk_id, d.calendar_month, d.calender_year order by d.calender_year, d.calendar_month, sale_vol DESC limit 10;""", value).mappings().all()
        if len(values) == 0:
            raise Exception("We have no data for Month {} Year {}".format(value["calendar_month"], value["calender_year"]))
        return values

    def getBookTypesEachUser(self, value):
        values = self.executeRawSql("""select fs.title, fs.first_name, fs.last_name, fs.date_of_birth, fs.street_address, fs.phone, b.type, count(b.type) as count from transfer t, freq_shopper fs, book b where t.shopper_id = fs.shopper_id and t.book_key = b.book_key and fs.shopper_id=:shopper_id group by b.type, fs.title, fs.first_name, fs.last_name, fs.date_of_birth, fs.street_address, fs.phone order by count desc;""", value).mappings().all()
        if len(values) == 0:
            raise Exception("We see zero transfer for {}".format(value["shopper_id"]))
        return values


    # def updateAssignment(self, value):
    #     return self.executeRawSql("""UPDATE assignment SET email=:email WHERE isbn=:isbn;""", value)
    
    # def addAssignment(self, value):
    #     return self.executeRawSql("""INSERT INTO assignment(email, isbn) VALUES(:email, :isbn);""", value)

    # def deleteAssignment(self, value):
    #     return self.executeRawSql("DELETE FROM assignment where email=:email and isbn=:isbn;", value)

    # def getAssignment(self, value):
    #     values = self.executeRawSql("""SELECT * FROM assignment WHERE email=:email and isbn=:isbn;""", value).mappings().all()
    #     if len(values) == 0:
    #         raise Exception("Book {} has not been assignment by {}".format(value["isbn"], value["email"]))
    #     return values[0]

    # def getAllBooks(self):
    #     return self.executeRawSql("SELECT * FROM book;").mappings().all()

    # def getAllUsers(self):
    #     return self.executeRawSql("SELECT * FROM student;").mappings().all()

    # def getBooksAndAssignments(self):
    #     return self.executeRawSql("SELECT book.isbn, email, title, author FROM book LEFT JOIN assignment ON book.isbn = assignment.isbn;").mappings().all()

    def getManagerByEmail(self, email):
        values = self.executeRawSql("""SELECT * FROM manager WHERE email=:email;""", {"email": email}).mappings().all()
        if len(values) == 0:
            raise Exception("Manager {} does not exist".format(email))
        return values[0]

    # def getStudentByEmail(self, email):
    #     values = self.executeRawSql("""SELECT * FROM student WHERE email=:email;""", {"email": email}).mappings().all()
    #     if len(values) == 0:
    #         raise Exception("Student {} does not exist".format(email))
    #     return values[0]

    def createModels(self):
        self.executeRawSql(
        """CREATE TABLE IF NOT EXISTS manager (
            email TEXT PRIMARY KEY,
            password TEXT NOT NULL
        );
        """)

        self.executeRawSql(
        """CREATE TABLE IF NOT EXISTS book (
            book_key VARCHAR(50) primary key,
            Printshop  VARCHAR(50) not null,
            Writer VARCHAR(50) not null,
            Publication_date DATE not null,
            Type VARCHAR(31) not null,
            Book_name VARCHAR(200) unique not null,
            Price DECIMAL(5,2) not null
            );
        """)

        self.executeRawSql(
        """CREATE TABLE IF NOT EXISTS clerk (
            clerk_id VARCHAR(50) PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            gender VARCHAR(50) NOT NULL,
            email VARCHAR(50) NOT NULL,
            date_of_hire DATE NOT NULL
            );
        """)

        self.executeRawSql(
            """CREATE TABLE IF NOT EXISTS Date (
                Date_Key VARCHAR(50) primary key,
                Date_Time VARCHAR(50) not null,
                Day_of_Week VARCHAR(50) not null,
                Calendar_Month INT not null,
                Calender_Year INT not null,
                Holiday VARCHAR(50) not null,
                Weekday VARCHAR(50) not null
                );
            """)
        
        self.executeRawSql(
            """CREATE TABLE IF NOT EXISTS freq_shopper (
                shopper_id VARCHAR(50) PRIMARY KEY,
                title VARCHAR(50) NOT NULL,
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50) NOT NULL,
                gender VARCHAR(50) NOT NULL,
                date_of_birth DATE NOT NULL,
                city VARCHAR(50) NOT NULL,
                street_address VARCHAR(50) NOT NULL,
                phone VARCHAR(50) NOT NULL
                );
            """)

        self.executeRawSql(
            """CREATE TABLE IF NOT EXISTS promotions (
                promotion_key VARCHAR(20) PRIMARY KEY,
                promotion_name VARCHAR(20) NOT NULL,
                price_reduction_type NUMERIC(4,2) NOT NULL,
                promotion_media_type VARCHAR(16),
                promotion_cost INT NOT NULL,
                promotion_begin_date DATE NOT NULL,
                promotion_end_date DATE NOT NULL
                );
            """)

        self.executeRawSql(
            """CREATE TABLE IF NOT EXISTS stores (
                store_key VARCHAR(30) PRIMARY KEY,
                store_name VARCHAR(50),
                store_street_address VARCHAR(50),
                store_city VARCHAR(50),
                store_country VARCHAR(50),
                store_manager VARCHAR(50),
                selling_square_footage INT,
                first_open_date DATE
                );
            """)

        self.executeRawSql(
            """CREATE TABLE IF NOT EXISTS transfer (
                POS_transfer_id VARCHAR(50) primary key,
                date_key VARCHAR(50) references date(date_key),
                book_key VARCHAR(21) references book(book_key),
                clerk_id VARCHAR(50) references clerk(clerk_id),
                shopper_id VARCHAR(50) references freq_shopper(shopper_id),
                promotion_key VARCHAR(50) references promotions(promotion_key),
                store_key VARCHAR(50) references stores(store_key)
                );
            """)
# data = ( { "id": 1, "title": "The Hobbit", "primary_author": "Tolkien" },
    #              { "id": 2, "title": "The Silmarillion", "primary_author": "Tolkien" },
    #     )

    # statement = text("""INSERT INTO book(id, title, primary_author) VALUES(:id, :title, :primary_author)""")