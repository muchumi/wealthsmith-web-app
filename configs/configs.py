import psycopg2, os

class Config(object):
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

class ProductionConfig(Config):
    # DATABASE_URI = 'postgres://zoiehgyiogmztt:d9a7437072fd23125f2906c33a4350728960c747656011db91975f25e365760b@ec2-54-73-147-133.eu-west-1.compute.amazonaws.com:5432/d9bq2ckd4dgsdq'
    # DEBUG = False
    # SECRET_KEY = 'd9a7437072fd23125f2906c33a4350728960c747656011db91975f25e365760b'
    # RECAPTCHA_PUBLIC_KEY = '6LdzYu0aAAAAAMWB6knmv86r7kV6HN2XoTy54opG'
    # RECAPTCHA_PRIVATE_KEY = '6LdzYu0aAAAAABup8DxsZo1v01Bori2eiu_I-FkG'
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY')
    RECAPTCHA_PUBLIC_KEY=os.environ.get('RECAPTCHA_PUBLIC_KEY')
    # pass
    conn = psycopg2.connect("dbname='the-wealthsmith-db' user='postgres' host='localhost' password='12121994'")

class TestingConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    # TESTING = True
    pass