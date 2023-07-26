# Dilithium2 Wrapper
This is a python wrapper that uses the shared library created from the original pq-crystals dilithium C library. 
It provides a wrapper for the following functions
- `int pqcrystals_dilithium2_ref_keypair(uint8_t *pk, uint8_t *sk);`
- `int pqcrystals_dilithium2_ref_signature(uint8_t *sig, size_t *siglen, const uint8_t *m, size_t mlen, const uint8_t *sk);`
- `int pqcrystals_dilithium2_ref_verify(const uint8_t *sig, size_t siglen, const uint8_t *m, size_t mlen, const uint8_t *pk);`

# Python Functions
## verify(signature:bytes, message:bytes, public_key:bytes) -> Boolean
## sign(message, secret_key) -> signature:bytes
## genKeypair() -> (public_key:bytes, secret_key:bytes)