from ctypes import cdll, cast, create_string_buffer
from ctypes import c_int, c_ubyte, POINTER, c_uint8, c_size_t
import ctypes as ct  
# OQS_SIG_keypair(uint8_t *public_key, uint8_t *secret_key) 
dilithium2_PUBLICKEYBYTES = 1312
dilithium2_SECRETKEYBYTES = 2528
dilithium2_BYTES = 2420


libdil = cdll.LoadLibrary('libpqcrystals_dilithium2_ref.so')
dil_keypair = libdil.pqcrystals_dilithium2_ref_keypair
dil_verify = libdil.pqcrystals_dilithium2_ref_verify
dil_sign = libdil.pqcrystals_dilithium2_ref_signature


# # int pqcrystals_dilithium2_ref_keypair(uint8_t *pk, uint8_t *sk);
def genKeypair():
    public_key = create_string_buffer(1312)
    secret_key = create_string_buffer(2528)

    dil_keypair(ct.byref(public_key), ct.byref(secret_key))
    return bytes(public_key), bytes(secret_key)

# int pqcrystals_dilithium2_ref_signature(uint8_t *sig, size_t *siglen, const uint8_t *m, size_t mlen, const uint8_t *sk);
# message is in bytes. secret key is of ctype buffer. it is like malloc in C
# https://docs.python.org/3/library/ctypes.html#fundamental-data-types

def sign(message, secret_key):
    my_message = ct.create_string_buffer(message, len(message))
    message_len = ct.c_int(len(my_message))
    signature = ct.create_string_buffer(dilithium2_BYTES)
    sig_len = ct.c_int(dilithium2_BYTES)  # initialize to maximum signature size

    my_secret_key = ct.create_string_buffer(secret_key, dilithium2_SECRETKEYBYTES)

    rv = dil_sign(ct.byref(signature),ct.byref(sig_len), my_message, message_len, secret_key)
    return bytes(signature[:sig_len.value])


# OQS_API OQS_STATUS OQS_SIG_verify(const OQS_SIG *sig, const uint8_t *message, size_t message_len, const uint8_t *signature, size_t signature_len, const uint8_t *public_key);
# int pqcrystals_dilithium2_ref_verify(
# const uint8_t *sig, 
# size_t siglen, 
# const uint8_t *m, 
# size_t mlen, 
# const uint8_t *pk);



def verify(signature, message, public_key):
    my_message = ct.create_string_buffer(message, len(message))
    message_len = ct.c_int(len(my_message))

    my_signature = ct.create_string_buffer(signature, len(signature))

    sig_len = ct.c_int(len(my_signature))

    my_public_key = ct.create_string_buffer(public_key, dilithium2_PUBLICKEYBYTES)
    rv = dil_verify(my_signature,sig_len, my_message, message_len, my_public_key)
    if rv==0:
        return True
    else:
        return False


pk, sk = genKeypair()
print(pk)
message = b"Hello"

signature = sign(message,sk)

print(verify(signature, b"Helllllllllllllo", pk))