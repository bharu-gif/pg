import datetime
from integration.utility.auth import AESCipher


class PgService:
    # Sabpaisa Merchant credentials #
    client_code = "ISHW90"
    trans_user_name = "docboonindia_10730"
    trans_user_password = "ISHW90_SP10730"
    auth_key = "mUDbYT0tN208WRhR"
    auth_iv = "SRZUMujQ2gMTYN2f"

    def request(self):

        # Payer details
        payer_name = 'bhargav'
        name = 'battina'
        payer_mobile = '1234567891'
        payer_email = 'test@gmail.com'
        Address = 'Delhi'

        # transaction details
        client_txn_id = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
        #client_txn_id = ''
        amount = '10'
        amount_type = 'INR'
        channel_id = 'W'
        call_back_url = "http://127.0.0.1:8000/pg/response/"
        browser = 'English|24-bit|1080|1920|UTC+2'
        class1 = 'IIV'
        roll = '234'

        # UPI
        vpa = '6300459407@ybl'

        # card
        holder_name = 'bhargava'
        cardno = '4029484589897107'
        expM = '12'
        expY = '30'
        cvv = '234'
        cardtype = 'visa'


        #*** Normal *** #
        # url = "payerName=" + payer_name + "&payerEmail=" + payer_email + "&payerMobile=" + payer_mobile + \
        #     "&clientTxnId=" + client_txn_id + "&amount=" + amount + "&clientCode=" + self.client_code + \
        #     "&transUserName=" + self.trans_user_name + "&transUserPassword=" + self.trans_user_password + \
        #     "&callbackUrl=" + call_back_url + "&amountType=" + amount_type + "&channelId=" + channel_id +\
        #     "&udf1=" + class1 + "&udf2=" + roll + "&browserDetails=" + browser

        # # *** Card *** #
        url = "payerName=" + payer_name + "&payerEmail=" + payer_email + "&payerMobile=" + payer_mobile + \
              "&clientTxnId=" + client_txn_id + "&amount=" + amount + "&clientCode=" + self.client_code + \
              "&transUserName=" + self.trans_user_name + "&transUserPassword=" + self.trans_user_password + \
              "&callbackUrl=" + call_back_url + "&amountType=" + amount_type + "&channelId=" + channel_id + \
              "&udf1=" + class1 + "&udf2=" + roll + "&browserDetails=" + browser + \
              "&cardHolderName=" + holder_name + "&pan=" + cardno + "&cardExpMonth=" + expM + "&cardExpYear=" + expY +"&cvv=" + cvv + \
              "&cardType=" + cardtype + "&modeTransfer=DC_CARD_TRANSFER&byPassFlag=true"

        # *** UPI *** #
        # url = "payerName=" + payer_name + "&payerEmail=" + payer_email + "&payerMobile=" + payer_mobile + \
        #       "&clientTxnId=" + client_txn_id + "&amount=" + amount + "&clientCode=" + self.client_code + \
        #       "&transUserName=" + self.trans_user_name + "&transUserPassword=" + self.trans_user_password + \
        #       "&callbackUrl=" + call_back_url + "&amountType=" + amount_type + "&channelId=" + channel_id + \
        #       "&udf1=" + class1 + "&udf2=" + roll + "&browserDetails=" + browser + "&payerVpa=" + vpa + \
        #       "&modeTransfer=UPI_MODE_TRANSFER&byPassFlag=true"

        # *** BHIM QR *** #
        # url = "payerName=" + payer_name + "&payerEmail=" + payer_email + "&payerMobile=" + payer_mobile + \
        #       "&clientTxnId=" + client_txn_id + "&amount=" + amount + "&clientCode=" + self.client_code + \
        #       "&transUserName=" + self.trans_user_name + "&transUserPassword=" + self.trans_user_password + \
        #       "&callbackUrl=" + call_back_url + "&amountType=" + amount_type + "&channelId=" + channel_id + \
        #       "&udf1=" + class1 + "&udf2=" + roll + "&browserDetails=" + browser + \
        #       "&modeTransfer=BHIM_UPI_QR_MODE_TRANSFER&byPassFlag=true"

        # *** Static BHIM QR *** #
        # url = "payerName=" + payer_name + "&payerEmail=" + payer_email + "&payerMobile=" + payer_mobile + \
        #       "&clientTxnId=" + client_txn_id + "&amount=" + amount + "&clientCode=" + self.client_code + \
        #       "&transUserName=" + self.trans_user_name + "&transUserPassword=" + self.trans_user_password + \
        #       "&callbackUrl=" + call_back_url + "&amountType=" + amount_type + "&channelId=" + channel_id + \
        #       "&udf1=" + class1 + "&udf2=" + roll + "&browserDetails=" + browser + \
        #       "&modeTransfer=STATIC_QR_MODE_TRANSFER&byPassFlag=true"

        enc_data = AESCipher(self.auth_key, self.auth_iv).encrypt(url)
        enc_data = enc_data.decode("utf-8")
        return enc_data

    def res(self, enc_response):
        dec_data = AESCipher(self.auth_key, self.auth_iv).decrypt(enc_response)
        print("dec response: ", dec_data)
        return dec_data.split("&")
