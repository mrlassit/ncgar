import OpenSSL
from twisted.internet import ssl

SECURE_CIPHERS = ':'.join(['ECDHE-RSA-AES256-GCM-SHA384',
 'ECDHE-ECDSA-AES256-GCM-SHA384',
 'ECDHE-RSA-AES256-SHA384',
 'ECDHE-ECDSA-AES256-SHA384',
 'ECDHE-RSA-AES256-SHA',
 'ECDHE-ECDSA-AES256-SHA',
 'SRP-DSS-AES-256-CBC-SHA',
 'SRP-RSA-AES-256-CBC-SHA',
 'SRP-AES-256-CBC-SHA',
 'DHE-DSS-AES256-GCM-SHA384',
 'DHE-RSA-AES256-GCM-SHA384',
 'DHE-RSA-AES256-SHA256',
 'DHE-DSS-AES256-SHA256',
 'DHE-RSA-AES256-SHA',
 'DHE-DSS-AES256-SHA',
 'DHE-RSA-CAMELLIA256-SHA',
 'DHE-DSS-CAMELLIA256-SHA',
 'ECDH-RSA-AES256-GCM-SHA384',
 'ECDH-ECDSA-AES256-GCM-SHA384',
 'ECDH-RSA-AES256-SHA384',
 'ECDH-ECDSA-AES256-SHA384',
 'ECDH-RSA-AES256-SHA',
 'ECDH-ECDSA-AES256-SHA',
 'AES256-GCM-SHA384',
 'AES256-SHA256',
 'AES256-SHA',
 'CAMELLIA256-SHA',
 'PSK-AES256-CBC-SHA',
 'ECDHE-ECDSA-DES-CBC3-SHA',
 'SRP-DSS-3DES-EDE-CBC-SHA',
 'SRP-RSA-3DES-EDE-CBC-SHA',
 'SRP-3DES-EDE-CBC-SHA',
 'EDH-RSA-DES-CBC3-SHA',
 'EDH-DSS-DES-CBC3-SHA',
 'ECDH-RSA-DES-CBC3-SHA',
 'ECDH-ECDSA-DES-CBC3-SHA',
 'DES-CBC3-SHA',
 'PSK-3DES-EDE-CBC-SHA',
 'ECDHE-RSA-AES128-GCM-SHA256',
 'ECDHE-ECDSA-AES128-GCM-SHA256',
 'ECDHE-RSA-AES128-SHA256',
 'ECDHE-ECDSA-AES128-SHA256',
 'ECDHE-RSA-AES128-SHA',
 'ECDHE-ECDSA-AES128-SHA',
 'SRP-DSS-AES-128-CBC-SHA',
 'SRP-RSA-AES-128-CBC-SHA',
 'SRP-AES-128-CBC-SHA',
 'DHE-DSS-AES128-GCM-SHA256',
 'DHE-RSA-AES128-GCM-SHA256',
 'DHE-RSA-AES128-SHA256',
 'DHE-DSS-AES128-SHA256',
 'DHE-RSA-AES128-SHA',
 'DHE-DSS-AES128-SHA',
 'DHE-RSA-SEED-SHA',
 'DHE-DSS-SEED-SHA',
 'DHE-RSA-CAMELLIA128-SHA',
 'DHE-DSS-CAMELLIA128-SHA',
 'ECDH-RSA-AES128-GCM-SHA256',
 'ECDH-ECDSA-AES128-GCM-SHA256',
 'ECDH-RSA-AES128-SHA256',
 'ECDH-ECDSA-AES128-SHA256',
 'ECDH-RSA-AES128-SHA',
 'ECDH-ECDSA-AES128-SHA',
 'AES128-GCM-SHA256',
 'AES128-SHA256',
 'AES128-SHA',
 'SEED-SHA',
 'CAMELLIA128-SHA',
 'PSK-AES128-CBC-SHA',
 'EDH-RSA-DES-CBC-SHA',
 'EDH-DSS-DES-CBC-SHA',
 'DES-CBC-SHA'])

class CustomOpenSSLContextFactory(ssl.DefaultOpenSSLContextFactory):
    def __init__(self, privateKeyFileName, certificateChainFileName,
                 sslmethod=OpenSSL.SSL.SSLv23_METHOD):
        self.privateKeyFileName = privateKeyFileName
        self.certificateChainFileName = certificateChainFileName
        self.sslmethod = sslmethod
        self.cacheContext()

    def cacheContext(self):
        ctx = OpenSSL.SSL.Context(self.sslmethod)
        ctx.use_certificate_chain_file(self.certificateChainFileName)
        ctx.use_privatekey_file(self.privateKeyFileName)
        ctx.set_options(OpenSSL.SSL.OP_NO_SSLv2)
        ctx.set_options(OpenSSL.SSL.OP_NO_SSLv3)
        ctx.set_cipher_list(SECURE_CIPHERS)
        self._context = ctx
