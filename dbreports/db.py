import DBcm

config = {
	"user": "druguser",
	"password": "drugpasswd",
	"host": "localhost",
	"database": "drugsdb",
	}

def get_orphan_count():
	with DBcm.UseDatabase(config) as cursor:
		SQL = """select count(*) from scraped where orphan = 1"""
		cursor.execute(SQL)
		data = cursor.fetchall()
	return data

def get_first_ten():
	with DBcm.UseDatabase(config) as cursor:
		SQL = """select * from scraped limit 10"""
		cursor.execute(SQL)
		data = cursor.fetchall()
	return data