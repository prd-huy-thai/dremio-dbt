from mimesis import Field, Fieldset, Schema, Text
from mimesis.enums import Gender, TimestampFormat
from mimesis.locales import Locale

field = Field(Locale.EN, seed=0xff)
fieldset = Fieldset(Locale.EN, seed=0xff)
text_generator = Text(Locale.EN, seed=0xff)

ORDER_STATUS = ['placed', 'shipped', 'completed', 'returned', 'return_pending']
PAYMENT_METHODS= ['credit_card', 'bank_transfer', 'coupon', 'gift_card']
TOTAL_CUSTOMER = 1000000
TOTAL_ORDERS = 10000000
TOTAL_PAYMENTS = 1000000


customer_schema = lambda: {
    "id": field("increment"),
    "first_name": field("person.name"),
    "last_name": field('random.generate_string_by_mask', mask='@.', char='@'),
}

order_schema = lambda: {
    "id": field("increment"),
    "user_id": field("integer_number", start=1, end=TOTAL_CUSTOMER),
    "order_date": field("date", start=2024, end=2024),
    "status": field("random.choice_enum_item", enum=ORDER_STATUS),
}

payment_schema = lambda: {
    "id": field("increment"),
    "order_id": field("integer_number", start=1, end=TOTAL_ORDERS),
    "payment_method": field("random.choice_enum_item", enum=PAYMENT_METHODS),
    "amount": field("integer_number", start=0, end=10000),

}


customers = Schema(schema=customer_schema, iterations=TOTAL_CUSTOMER)
orders = Schema(schema=order_schema, iterations=TOTAL_ORDERS)
payements = Schema(schema=payment_schema, iterations=TOTAL_PAYMENTS)


customers.to_csv(file_path='seeds/raw_customers.csv')
print('raw_customers.csv Done !!!')
orders.to_csv(file_path='seeds/raw_orders.csv')
print('raw_orders.csv Done !!!')
payements.to_csv(file_path='seeds/raw_payments.csv')
print('raw_payments.csv Done !!!')
print('Done !!!')