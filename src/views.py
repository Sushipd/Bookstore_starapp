from flask import request, session, redirect, url_for, render_template, flash

from . models import Models
from . forms import BestBooksForm, BestClerksForm, BookTypesForm, SalesForm, MostFreqShopperForm, AddBookForm, AddClerkForm, AddDateForm, AddFreqShopperForm, AddPromotionForm, AddStoreForm, AddTransferForm, SignUpForm, SignInForm 
# AddReaderForm, 

from src import app

models = Models()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/promotionFeatures')
def promotionFeatures():
    try:
        if session['user_available']:
            promotionFeatures = models.getPromotionFeatures()
            return render_template('promotionFeatures.html', promotionFeatures=promotionFeatures)
        flash('User is not Authenticated')
        return redirect(url_for('index'))
    except Exception as e:
        flash(str(e))


@app.route('/transfers')
def transfers():
    try:
        if session['user_available']:
            transfers = models.getTransfers()
            return render_template('transfers.html', transfers=transfers)
        flash('User is not Authenticated')
        return redirect(url_for('index'))
    except Exception as e:
        flash(str(e))


@app.route('/bestBooks', methods=['GET', 'POST'])
def bestBooks():
    try:
        if session['user_available']:
            reader = BestBooksForm(request.form)
            if request.method == 'POST':
                bestBooks = models.getBestSellersEachMonth({"calendar_month": reader.calendar_month.data, "calender_year": reader.calender_year.data})
                return render_template('bestBooks2.html', bestBooks=bestBooks)
            return render_template('bestBooks.html', reader=reader)
    except Exception as e:
        flash(str(e))
    flash('User is not Authenticated')
    return redirect(url_for('index'))


@app.route('/bestClerks', methods=['GET', 'POST'])
def bestClerks():
    try:
        if session['user_available']:
            reader = BestClerksForm(request.form)
            if request.method == 'POST':
                bestClerks = models.getBestClerksEachMonth({"calendar_month": reader.calendar_month.data, "calender_year": reader.calender_year.data})
                return render_template('bestClerks2.html', bestClerks=bestClerks)
            return render_template('bestClerks.html', reader=reader)
    except Exception as e:
        flash(str(e))
    flash('User is not Authenticated')
    return redirect(url_for('index'))


@app.route('/bookTypes', methods=['GET', 'POST'])
def bookTypes():
    try:
        if session['user_available']:
            reader = BookTypesForm(request.form)
            if request.method == 'POST':
                bookTypes = models.getBookTypesEachUser({"shopper_id": reader.shopper_id.data})
                return render_template('bookTypes2.html', bookTypes=bookTypes)
            return render_template('bookTypes.html', reader=reader)
    except Exception as e:
        flash(str(e))
    flash('User is not Authenticated')
    return redirect(url_for('index'))


@app.route('/sales', methods=['GET', 'POST'])
def sales():
    try:
        if session['user_available']:
            reader = SalesForm(request.form)
            if request.method == 'POST':
                salesAmount = models.getSalesEachMonthForStore({"store_key": reader.store_key.data})
                return render_template('sales2.html', salesAmount=salesAmount)
            return render_template('sales.html', reader=reader)
    except Exception as e:
        flash(str(e))
    flash('User is not Authenticated')
    return redirect(url_for('index'))


@app.route('/mostFreqShopper', methods=['GET', 'POST'])
def mostFreqShopper():
    try:
        if session['user_available']:
            reader = MostFreqShopperForm(request.form)
            if request.method == 'POST':
                mostFreqShopper = models.getMostFreqShopperForStore({"store_key": reader.store_key.data})
                return render_template('mostFreqShopper2.html', mostFreqShopper=mostFreqShopper)
            return render_template('mostFreqShopper.html', reader=reader)
    except Exception as e:
        flash(str(e))
    flash('User is not Authenticated')
    return redirect(url_for('index'))


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
                return redirect(url_for('transfers'))
            return render_template('addTransfers.html', reader=reader)
    except Exception as e:
        flash(str(e))
    flash('User is not Authenticated')
    return redirect(url_for('index'))


@app.route('/delete/<pos_transfer_id>', methods=('GET', 'POST'))
def delete_transfer(pos_transfer_id):
    try:
        models.deleteTransfer({"pos_transfer_id": pos_transfer_id})
        return redirect(url_for('transfers'))
    except Exception as e:
        flash(str(e))
        return redirect(url_for('index'))


@app.route('/updateTransfers/<date_key>/<book_key>/<clerk_id>/<shopper_id>/<promotion_key>/<store_key>/<POS_transfer_id>', methods=('GET', 'POST'))
def update_transfer(date_key,book_key,clerk_id,shopper_id,promotion_key,store_key,POS_transfer_id):
    try:
        br = models.getTransfer({"pos_transfer_id": POS_transfer_id})
        reader = AddTransferForm(request.form, obj=br)
        if request.method == 'POST':
            models.updateTransfer({"pos_transfer_id": reader.POS_transfer_id.data, "date_key": reader.date_key.data, "book_key": reader.book_key.data, "clerk_id": reader.clerk_id.data, "shopper_id": reader.shopper_id.data, "promotion_key": reader.promotion_key.data, "store_key": reader.store_key.data})
            return redirect(url_for('transfers'))
        return render_template('updateTransfers.html', reader=reader)
    except Exception as e:
        flash(str(e))
        return redirect(url_for('index'))


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
                return redirect(url_for('transfers'))
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
