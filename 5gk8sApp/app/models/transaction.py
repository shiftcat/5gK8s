from app import db


class TxHist(db.Model):

    __tablename__ = "TX_HIST"

    id = db.Column(db.Integer, primary_key=True)

    method = db.Column(db.String(15))

    resource = db.Column(db.String(300))

    remote_addr = db.Column(db.String(150))

    agent = db.Column(db.String(300))

    data = db.Column(db.String(20000))

    tx_date = db.Column(db.Date)


    def to_json(self):
        json = {
            "id": self.id,
            "method": self.method,
            "resource": self.resource,
            "data": self.data,
            "tx_data": self.tx_date.strftime('%Y-%m-%d') if self.tx_date is not None else None,
        }
        return json