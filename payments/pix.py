import uuid
import qrcode

class Pix:
    def __init__(self):
        pass
    
    def create_payment(self):
        
        #Criar o pagamento na instituição)
        bank_payment_id = str(uuid.uuid4())
        
        #codigo copia e cola
        hash_payment = f'hash_payment_{bank_payment_id}'
        
        #qr code
        img = qrcode.make(hash_payment)
        
        #salva a imagem
        img.save(f"static/img/qr_code_{bank_payment_id}.png")  # type: ignore

        return {"bank_payment_id":bank_payment_id,"qr_code_path":f"qr_code_path{bank_payment_id}"}
        