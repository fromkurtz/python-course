import os
import pymysql
import dotenv

TABLE_NAME = 'customers'

dotenv.load_dotenv()


connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
)

with connection:
    with connection.cursor() as cursor:
        # Cria a tabela se não existir
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            '  `id` INT NOT NULL AUTO_INCREMENT,'
            '  `name` VARCHAR(45) NOT NULL,'
            '  `age` INT NOT NULL,'
            '  PRIMARY KEY (`id`))'
        )
        
        # ⚠️ CUIDADO: ISSO APAGA TODOS OS DADOS!
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
    connection.commit()

    with connection.cursor() as cursor:
        # Inserção 1 (usando tupla)
        sql = f'INSERT INTO {TABLE_NAME} (`name`, `age`) VALUES (%s, %s)'
        cursor.execute(sql, ('Lucas', 30))
        print("Inserido Lucas, 30")

        # Inserção 2 (usando dicionário)
        sql = f'INSERT INTO {TABLE_NAME} (`name`, `age`) VALUES (%(name)s, %(age)s)'
        cursor.execute(sql, {"name": "Le", "age": 50})
        print("Inserido Le, 50")
    connection.commit()
