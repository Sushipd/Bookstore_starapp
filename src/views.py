from flask import request, session, redirect, url_for, render_template, flash

from . models import Models
from . forms import AddBookForm, AddClerkForm, AddDateForm, AddFreqShopperForm, AddPromotionForm, AddStoreForm, AddTransferForm, SignUpForm, SignInForm 
# AddReaderForm, 

from src import app

models = Models()

@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/books')
# def show_books():
#     try:
#         if session['user_available']:
#             booksAndAssignments = models.getBooksAndAssignments()
#             return render_template('books.html', booksAndAssignments=booksAndAssignments)
#         flash('User is not Authenticated')
#         return redirect(url_for('index'))
#     except Exception as e:
#         flash(str(e))


# @app.route('/add', methods=['GET', 'POST'])
# def add_reader():
#     try:
#         if session['user_available']:
#             reader = AddReaderForm(request.form)
#             if request.method == 'POST':
#                 models.addAssignment({"email": reader.email.data, "isbn": reader.isbn.data})
#                 return redirect(url_for('show_books'))
#             return render_template('add.html', reader=reader)
#     except Exception as e:
#         flash(str(e))
#     flash('User is not Authenticated')
#     return redirect(url_for('index'))


@app.route('/addStores', methods=['GET', 'POST'])
def add_store():
    try:
        if session['user_available']:
            reader = AddStoreForm(request.form)
            if request.method == 'POST':
                models.addStores({"store_key": reader.store_key.data, "store_name": reader.store_name.data, "store_street_address": reader.store_street_address.data, "store_city": reader.store_city.data, "store_country": reader.store_country.data, "store_manager": reader.store_manager.data, "selling_square_footage": reader.selling_square_footage.data,"first_open_date": reader.first_open_date.data})
                #return redirect(url_for('show_books'))
            return render_template('addStores.html', reader=reader)
    except Exception as e:
        flash(str(e))
    flash('User is not Authenticated')
    return redirect(url_for('index'))


# @app.route('/addDate', methods=['GET', 'POST'])
# def add_date():
#     try:
#         if session['user_available']:
#             reader = AddReaderForm(request.form)
#             if request.method == 'POST':
#                 models.addDate({"Date_Key": reader.Date_Key.data, "Date_Time": reader.Date_Time.data, "Day_of_Week": reader.Day_of_Week.data, "Calendar_Month": reader.Calendar_Month.data, "Calender_Year": reader.Calender_Year.data, "Holiday": reader.Holiday.data, "Weekday": reader.Weekday.data})
#                 #return redirect(url_for('show_books'))
#             return render_template('addDate.html', reader=reader)
#     except Exception as e:
#         flash(str(e))
#     flash('User is not Authenticated')
#     return redirect(url_for('index'))


@app.route('/addBook', methods=['GET', 'POST'])
def add_book():
    try:
        if session['user_available']:
            reader = AddBookForm(request.form)
            if request.method == 'POST':
                models.addBook({"book_key": reader.book_key.data, "Printshop": reader.Printshop.data,"Writer":reader.Writer.data,"Publication_date":reader.Publication_date.data,"Type":reader.Type.data,"Book_name":reader.Book_name.data, "Price":reader.Price.data})
                #return redirect(url_for('show_books'))
            return render_template('addBook.html', reader=reader)
    except Exception as e:
        flash(str(e))
    flash('User is not Authenticated')
    return redirect(url_for('index'))


@app.route('/addClerk', methods=['GET', 'POST'])
def add_clerk():
    try:
        if session['user_available']:
            reader = AddClerkForm(request.form)
            if request.method == 'POST':
                models.addClerk({"clerk_id": reader.clerk_id.data, "first_name": reader.first_name.data,"last_name":reader.last_name.data,"gender":reader.gender.data,"email":reader.email.data,"date_of_hire":reader.date_of_hire.data})
                #return redirect(url_for('show_clerks'))
            return render_template('addClerk.html', reader=reader)
    except Exception as e:
        flash(str(e))
    flash('User is not Authenticated')
    return redirect(url_for('index'))


# @app.route('/addPromotion', methods=['GET', 'POST'])
# def add_promotion():
#     try:
#         if session['user_available']:
#             reader = AddReaderForm(request.form)
#             if request.method == 'POST':
#                 models.addpromotion({"promotion_key": reader.promotion_key.data, "promotion_name": reader.promotion_name.data, "price_reduction_type": reader.price_reduction_type.data,"promotion_media_type":reader.promotion_media_type.data,"promotion_cost":reader.promotion_cost.data,"promotion_begin_date":reader.promotion_begin_date.data,"promotion_end_date":reader.promotion_end_date.data})
#                 #return redirect(url_for('show_promotions'))
#             return render_template('addPromotion.html', reader=reader)
#     except Exception as e:
#         flash(str(e))
#     flash('User is not Authenticated')
#     return redirect(url_for('index'))
    

@app.route('/addFreqshopper', methods=['GET', 'POST'])
def add_freqshopper():
    try:
        if session['user_available']:
            reader = AddFreqShopperForm(request.form)
            if request.method == 'POST':
                models.addFreqShopper({"shopper_id": reader.shopper_id.data, "title": reader.title.data, "first_name": reader.first_name.data, "last_name": reader.last_name.data, "gender": reader.gender.data, "date_of_birth": reader.date_of_birth.data, "city": reader.city.data, "street_address": reader.street_address.data, "phone": reader.phone.data})
                #return redirect(url_for('show_books'))
            return render_template('addFreqshopper.html', reader=reader)
    except Exception as e:
        flash(str(e))
    flash('User is not Authenticated')
    return redirect(url_for('index'))


@app.route('/addTransfers', methods=['GET', 'POST'])
def add_transfers():
    try:
        if session['user_available']:
            reader = AddTransferForm(request.form)
            if request.method == 'POST':
                models.addTransfer({"POS_transfer_id": reader.POS_transfer_id.data, "date_key": reader.date_key.data, "book_key": reader.book_key.data, "clerk_id": reader.clerk_id.data, "shopper_id": reader.shopper_id.data, "promotion_key": reader.promotion_key.data, "store_key": reader.store_key.data})
                #return redirect(url_for('show_books'))
            return render_template('addTransfers.html', reader=reader)
    except Exception as e:
        flash(str(e))
    flash('User is not Authenticated')
    return redirect(url_for('index'))


# @app.route('/delete/<email>/<isbn>', methods=('GET', 'POST'))
# def delete_book(isbn, email):
#     try:
#         models.deleteAssignment({"email": email, "isbn": isbn})
#         return redirect(url_for('show_books'))
#     except Exception as e:
#         flash(str(e))
#         return redirect(url_for('index'))


# @app.route('/update/<email>/<isbn>', methods=('GET', 'POST'))
# def update_book(isbn, email):
#     try:
#         br = models.getAssignment({"email": email, "isbn": isbn})
#         reader = AddReaderForm(request.form, obj=br)
#         if request.method == 'POST':
#             models.updateAssignment({"email": reader.email.data, "isbn": reader.isbn.data})
#             return redirect(url_for('show_books'))
#         return render_template('update.html', reader=reader)
#     except Exception as e:
#         flash(str(e))
#         return redirect(url_for('index'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    try:
        signupform = SignUpForm(request.form)
        if request.method == 'POST':
            models.addUsers({"email": signupform.email.data, "password": signupform.password.data})
            return redirect(url_for('signin'))
        return render_template('signup.html', signupform=signupform)
    except Exception as e:
        flash(str(e))
        return redirect(url_for('index'))


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    try:
        signinform = SignInForm(request.form)
        if request.method == 'POST':
            em = signinform.email.data
            log = models.getManagerByEmail(em)
            if log.password == signinform.password.data:
                session['current_user'] = em
                session['user_available'] = True
                # return redirect(url_for('show_books'))
                return redirect(url_for('about_user'))
            else:
                flash('Cannot sign in')
        return render_template('signin.html', signinform=signinform)
    except Exception as e:
        flash(str(e))
        return redirect(url_for('index'))


@app.route('/about_user')
def about_user():
    try:
        if session['user_available']:
            user = models.getManagerByEmail(session['current_user'])
            return render_template('about_user.html', user=user)
        flash('You are not a Authenticated User')
        return redirect(url_for('index'))
    except Exception as e:
        flash(str(e))
        return redirect(url_for('index'))


@app.route('/logout')
def logout():
    try:
        session.clear()
        session['user_available'] = False
        return redirect(url_for('index'))
    except Exception as e:
        flash(str(e))
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
