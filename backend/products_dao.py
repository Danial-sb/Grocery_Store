from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()
    query = ("select products.product_id, products.product_name, products.uom_id, products.price_per_unit, uom.uom_name from products inner join uom on products.uom_id=uom.uom_id")
    cursor.execute(query)
    response = []
    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            'product_id': product_id,
            'name': name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name
        })
    return response 


def add_product(connection, product):
    cursor = connection.cursor()

    query = ("INSERT INTO products (product_name, uom_id, price_per_unit) VALUES (%s, %s, %s)")

    data = (product['product_name'], product['uom_id'], product['price_per_unit'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid


def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ('Delete from products where product_id=' + str(product_id))
    cursor.execute(query)
    connection.commit()

#def edit(connection, product_id, product_name, uom_id, price_per_unit):
 #   cursor = connection.cursor()
   # query = ('Update products Set product_name = ' +str(product_name) + ', uom_id =' +str(uom_id)+ ',price_per_unit ='+str(price_per_unit) + 'where product_id='+ product_id)
    #cursor.execute(query)
    #connection.commit()


if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_all_products(connection))
    #print(add_product(connection, {
        #'product_name' : 'potato',
        #'uom_id' : '2',
        #'price_per_unit' : '12000'
    #}))
    #print(delete_product(connection, 8))

    #print(edit(connection, '1', 'pepper', '1', '2000'))