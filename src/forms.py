from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, BooleanField, EmailField, DateField, IntegerField, DecimalField
from wtforms.validators import DataRequired, Length, Email, ValidationError

def length_check(form,field):
    if len(field.data) == 0:
        raise ValidationError('Fields should not be null')
    

# class AddReaderForm(Form):
#     email = StringField('Email', validators=[ DataRequired()])
#     isbn = StringField('ISBN', validators = [DataRequired()])

class BestBooksForm(Form):
    calendar_month = StringField('Calendar month', validators = [DataRequired()])
    calender_year = StringField('Calendar year', validators=[ DataRequired()])

class BestClerksForm(Form):
    calendar_month = StringField('Calendar month', validators = [DataRequired()])
    calender_year = StringField('Calendar year', validators=[ DataRequired()])

class AddBookForm(Form):
    book_key = StringField('Book key', validators=[ DataRequired()])
    Printshop = StringField('Print shop', validators = [DataRequired()])
    Writer = StringField('Writer', validators=[ DataRequired()])
    Publication_date = DateField('Publication date', validators = [DataRequired()])
    Type = StringField('Type', validators=[ DataRequired()])
    Book_name = StringField('Book name', validators = [DataRequired()])
    Price = DecimalField('Price', validators=[ DataRequired()])

class AddClerkForm(Form):
    clerk_id = StringField('Clerk ID', validators=[ DataRequired()])
    first_name = StringField('First name', validators = [DataRequired()])
    last_name = StringField('Last name', validators=[ DataRequired()])
    gender = StringField('Gender', validators = [DataRequired()])
    email = StringField('Email', validators=[ DataRequired()])
    date_of_hire = DateField('Date of hire', validators = [DataRequired()])

class AddDateForm(Form):
    Date_Key = StringField('Date key', validators=[ DataRequired()])
    Date_Time = StringField('Date time', validators = [DataRequired()])
    Day_of_Week = StringField('Day of week', validators=[ DataRequired()])
    Calendar_Month = StringField('Calendar month', validators = [DataRequired()])
    Calender_Year = StringField('Calendar year', validators=[ DataRequired()])
    Holiday = StringField('Holiday', validators = [DataRequired()])
    Weekday = StringField('Weekday', validators=[ DataRequired()])

class AddFreqShopperForm(Form):
    shopper_id = StringField('Shopper ID', validators=[ DataRequired()])
    title = StringField('Title', validators = [DataRequired()])
    first_name = StringField('First name', validators=[ DataRequired()])
    last_name = StringField('Last name', validators = [DataRequired()])
    gender = StringField('Gender', validators=[ DataRequired()])
    date_of_birth = DateField('Date of birth', validators=[ DataRequired()])
    city = StringField('City', validators = [DataRequired()])
    street_address = StringField('Street address', validators=[ DataRequired()])
    phone = StringField('Phone', validators = [DataRequired()])

class AddPromotionForm(Form):
    promotion_key = StringField('Promotion key', validators=[ DataRequired()])
    promotion_name = StringField('Promotion name', validators=[ DataRequired()])
    price_reduction_type = IntegerField('Price reduction type', validators = [DataRequired()])
    promotion_media_type = StringField('Promotion media type', validators=[ DataRequired()])
    promotion_cost = IntegerField('Promotion cost', validators = [DataRequired()])
    promotion_begin_date = DateField('Promotion begin date', validators=[ DataRequired()])
    promotion_end_date = DateField('Promotion end date', validators = [DataRequired()])

class AddStoreForm(Form):
    store_key = StringField('Store key', validators=[ DataRequired()])
    store_name = StringField('Store name', validators = [DataRequired()])
    store_street_address = StringField('Store street address', validators = [DataRequired()])
    store_city = StringField('Store city', validators=[ DataRequired()])
    store_country = StringField('Store country', validators = [DataRequired()])
    store_manager = StringField('Store manager', validators=[ DataRequired()])
    selling_square_footage = IntegerField('Selling square footage', validators = [DataRequired()])
    first_open_date = DateField('First open date', validators=[ DataRequired()])

class AddTransferForm(Form):
    POS_transfer_id = StringField('POS transfer ID', validators=[ DataRequired()])
    date_key = StringField('Date key', validators = [DataRequired()])
    book_key = StringField('Book key', validators=[ DataRequired()])
    clerk_id = StringField('Clerk ID', validators = [DataRequired()])
    shopper_id = StringField('Shopper ID', validators=[ DataRequired()])
    promotion_key = StringField('Promotion key', validators = [DataRequired()])
    store_key = StringField('Store key', validators=[ DataRequired()])


class SignUpForm(Form):
    password = PasswordField('Password',validators=[ DataRequired(), Length(min=6)])
    email = EmailField('Email', validators= [DataRequired(), Email()])
    submit = SubmitField('Sign Up')


class SignInForm(Form):
    email = EmailField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired(), Length(min=6, max=30)])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Sign In')
