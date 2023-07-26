from ctypes import cdll, cast, create_string_buffer
from ctypes import c_int, c_ubyte, POINTER
import numpy as np

# load the shared library containing the C function
libkyber = cdll.LoadLibrary('libpqcrystals_kyber512_ref.so')

pqcrystals_kyber512_ref_keypair = libkyber.pqcrystals_kyber512_ref_keypair
pqcrystals_kyber512_ref_keypair.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte)]
pqcrystals_kyber512_ref_keypair.restype = c_int
pk = create_string_buffer(800)
sk = create_string_buffer(1632)

# pass pointers to unsigned bytes to the function
pk_ptr = cast(pk, POINTER(c_ubyte))
sk_ptr = cast(sk, POINTER(c_ubyte))

pqcrystals_kyber512_ref_keypair(pk_ptr, sk_ptr)
pk_list = [int.from_bytes(pk[i:i+1], byteorder='little') for i in range(len(pk))]
sk_list = [int.from_bytes(sk[i:i+1], byteorder='little') for i in range(len(sk))]

print('pk:', pk_list)
print('sk:', sk_list)


#define pqcrystals_kyber512_SECRETKEYBYTES 1632
#define pqcrystals_kyber512_PUBLICKEYBYTES 800
#define pqcrystals_kyber512_CIPHERTEXTBYTES 768
#define pqcrystals_kyber512_BYTES 32