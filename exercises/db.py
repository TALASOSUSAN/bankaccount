table_name: str = None
table_value: str = None
table_col: str = None


def mainRun():
    tbl_name()
    tbl_col()
    tbl_value()
    print("\nResult...")
    create_db()
    insert_db()
    update_db()
    delete_db()
    select_db()


def create_db():
    print("CREATE TABLE {} ({})".format(table_name, table_col))


def insert_db():

    print("INSERT INTO {} ({}) VALUES ({})".format(table_name, table_col, table_value))


def update_db():
    tbl_colandvalue = col(table_value, table_col)
    print("UPDATE {} SET {}".format(table_name, tbl_colandvalue))


def delete_db():
    print("DELETE FROM {}".format(table_name, table_col))


def select_db():
    print("SELECT {1} FROM {0}".format(table_name, table_col))


def col(text, text_2):
    global col_value
    textr = text.rsplit(", ")
    textrr = text_2.rsplit(", ")
    col_0 = ""
    for i in range(len(textr)):
        col_0 += str(textrr[i]) + str(" = ") + str(textr[i]) + str("  ")
    col_1 = col_0.rsplit("  ")
    if  len(col_1)<=2:
      col_value = col_0
    else:
      col_value = ", ".join(col_1)
    return col_value


def data_db(text):
    text_split = text.split()
    text_join = ", ".join(text_split)
    return text_join


def tbl_name():
    global table_name
    print("++Enter Table Name++\nExample: tbl_member")
    table_name = input(">> ")


def tbl_col():
    global table_col
    print("++Enter Table Column++\nExample: id user pass name ban ip")
    text = input(">> ")
    table_col = data_db(text)


def tbl_value():
    global table_value
    print("++Enter Table Value++\nExample: null zemon 1234 zemonhunter true 127.0.0.1")
    text = input(">> ")
    table_value = data_db(text)

print("Create sql table quickly")
print("*Columns and Value must be equal.")
mainRun()