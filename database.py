from sqlalchemy import create_engine,text

db_Connection_String="mysql+pymysql://o5ve1bm8ci48kzkhua60:pscale_pw_of9opHyFiQgM1Fq1u37xIMsym1rg8U1ubEQRg2LFrw7@ap-south.connect.psdb.cloud/kshanikacareers?charset=utf8mb4"
engine =create_engine(db_Connection_String,
                      connect_args={
    "ssl":{
    "ssl_ca":"/etc/ssl/cert.pem"
    }
                      })

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        keys=tuple(result.keys())
        jobs=[]
        for row in result.all():
            jobs.append(dict(zip(keys,row)))
    return jobs

def load_job_from_db(id):
    with engine.connect() as conn:
        stmt=text("select * from jobs where id= :val")
        stmt=stmt.bindparams(val=id)
        result = conn.execute(stmt)
        rows=result.all()
        keys=tuple(result.keys())
    if len(rows) == 0:
        return None
    else:
        return dict(zip(keys,rows[0]))