from flask import Flask,jsonify,request
from repository.database import db
from db_models.payment import Payment
from datetime import datetime, timedelta
from payments.pix import Pix

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY']= 'SECRET_KEY_WEBSOCKET'



db.init_app(app)

@app.route('/payments/pix',methods=['POST'])
def create_payment_pix():
    
    data = request.get_json()
    
    #validações
    if 'value' not in data:
        return jsonify({"messagem":"Invalid value"}),400
    
    expiration_data = datetime.now() + timedelta(minutes=30)
    
    new_payment = new_payment = Payment(
                                        value=data['value'],
                                        expiration_date=expiration_data)
    
    
    pix_obj = Pix()
    data_payment_pix = pix_obj.create_payment()
    
    
    
    
    db.session.add(new_payment)
    db.session.commit()   
    
    return jsonify({
        "message": "The payment has been created",
        "payment": new_payment.to_dict()
    })







@app.route('/payments/pix/confirmation',methods=['POST'])
def pix_confirmation():
    return jsonify({"message":"The payment has been corfirmed"})









@app.route('/payments/pix/<int:payment_id>',methods=['GET'])
def payment_px_page(payment_id):
    return 'pagamento pix'




if __name__ == '__main__':
    app.run(debug=True)
