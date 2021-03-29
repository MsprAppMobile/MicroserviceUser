import connection

conn = connection.db_connection()

cursor = conn.cursor()
sql_database = """ DROP DATABASE beers; """
sql_database1 = """ CREATE DATABASE beers; """
sql_database2 = """ USE beers; """

sql_code= """CREATE table code (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    expiration_date DATETIME NOT NULL,
    image VARCHAR(300) NOT NULL,
    description TEXT NOT NULL,
    value INT NOT NULL,
    identifiant_QRCode VARCHAR(200) NOT NULL,
    is_unique BOOLEAN NOT NULL,
    category VARCHAR(300) NOT NULL);"""

sql_user = """ CREATE table `user` (
    id INT PRIMARY KEY AUTO_INCREMENT,
    pseudo VARCHAR(100) NOT NULL,
    mail VARCHAR(300) NOT NULL,
    password VARCHAR(100) NOT NULL,
    telephone VARCHAR(15) NOT NULL,
    genre VARCHAR(50) NOT NULL,
    codeP VARCHAR(20) NOT NULL,
    ville VARCHAR(100) NOT NULL,
    adresse VARCHAR(100) NOT NULL,
    complementAdresse VARCHAR(100),
    role VARCHAR(50) NOT NULL,
    CONSTRAINT UC_user_pseudo UNIQUE (pseudo));"""

sql_codelist = """CREATE table `codelist` (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    code_id INT NOT NULL,
    status BOOLEAN NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (code_id) REFERENCES code(id));"""
    
sql_adduser = """INSERT INTO user (pseudo,mail,password,telephone,genre,codeP,ville,adresse,role) values ('test','test@test.com','test','0240152585','Monsieur','44840','Les sorinières','45 rue de la fillaudière','admin'),
('florian','florian@civel.com','aze','0618002677','Madame','44100','Nantes','3 rue de hotel de ville','user');"""

sql_promo = """INSERT INTO code (name,expiration_date,image,description,value,identifiant_QRCode,is_unique,category) values 
('promotest','2021-03-27','iefhoezjfoijojvre.jpeg','Ceci est une promo test',30,'1254',true,'pourcentage'),
('promo2','2021-05-05','uihfoief.jpeg','Ceci est une autre promo',20,'identifiantcode',true,'remise');"""

sql_commit = """COMMIT;"""


cursor.execute(sql_database)
cursor.execute(sql_database1)
cursor.execute(sql_database2)
cursor.execute(sql_code)
cursor.execute(sql_user)
cursor.execute(sql_codelist)
cursor.execute(sql_adduser)
cursor.execute(sql_promo)
cursor.execute(sql_commit)
cursor.close()
conn.commit()
conn.close()

