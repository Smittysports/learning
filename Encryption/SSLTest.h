/** \page SSL_Encryption SSL Encryption
 * 
 * \section Acronyms
 * - SSL (Secure Socket Layer)
 * - TLS (Transport Layer Security)
 * 
 * \section Overview
 * 
 * Key exchange -> Data Encryption -> Handshake Integrity -> Server Authenticity (Certificates)
 * 
 * Secure communication is done with Public/Private key pairs. The server has a 'Private' key and
 * encrypts data with it. The server must send the associated 'Public' key to a client so that the
 * client can encrypt and decrypt messages when talking with the server.
 * 
 * There must be a secure way of getting the Public key to a client without it being intercepted. This
 * is the key exchange mechanism. TLS can be used for both encryption and key exchange.
 * 
 * A certificate is used in TLS to allow for key exchange.
 * 
 * \section Encryption Algorithms for Key exchange
 * - RSA            
 * - Diffie Hellman (Currently used for TLS 1.2, uses prime numbers)
 * - DHECE          (Currently used for TLS 1.3, Elliptical Curve Diffie Hellman Effemeral)
 * 
 * \section Encryption Algorithms for Data Encryption
 * - 3DES           (Not used)
 * - AES            (Can sign the encryption)
 * - ChaCha20       (Can sign the encryption)
 * 
 * \section Session keys
 * 
 * You can decrypt SSL traffic using SSL session keys. These can be obtained by setting the
 * SSLKEYLOGFILE environment variable to a location on your hard drive. This will work
 * with both RSA and Diffie-Hellman based key exchanges.
 * 
 * This requires either Firefox or Chrome.
 *
 * - Windows
 * -# Open the environment variables window
 * -# Create a new 'user variable' with a 'Variable name' of SSLKEYLOGFILE and a 'Variable value'
 * of the location to store the file (ex... C:\dev\sslkeys\sslkeylog.txt)
 * -# Start Wireshark and choose the network that the packets will be sent over
 * -# Start Firefox of Chrome and go to a webpage that is secured by HTTPS
 * -# Restart Wireshark, go to 'Edit->Preferences->Protocols->TLS', and put the sslkeylog.txt that was
 * described earlier into the '(Pre)-Master-Secret log filename
 * -# The SSL session is now decrypted
 * -# Note: use the filter 'frame.contains yahoo' to find all frames that are sent to yahoo
 * 
 * \section Key Exchange (Negotiation)
 * TLS (Transport Layer Security) is the transport protocol used for secure communication. It is referred
 * to as SSL because they were the original protocols used by Netscape Navigator. TLS evolved from SSL, which
 * is no longer safe.
 * 
 * TLS 1.2 and 1.3 are the most recent as of 9/19/2023. TLS 1.3 is more secure and utilize less overhead in
 * the handshake.
 * 
 * \subsection Diffie Hellman Encryption
 * 
 * TODO: Elaborate on this. The Diffie Hellman algorithm will add 2 prime numbers to a certificate and store a private
 * key locally that is used to raise one of the prime numbers to this number... as well as other things.
 * TODO: The Elliptical Curve Diffie Hellman will TBD.
 * 
 * \subsection Perfect Forward Secrecy
 * 
 * Perfect forward secrecy is used to 'guarantee' that if someone steals the data but does not have a key, they will
 * not be able to decypher it for a very long time since the math supposedly makes it impossible to figure it out.
 * 
 * \section Data Encryption Protocols (Ciphers)
 * 
 * These are used to encrypt the data once the key exchange is complete.
 * 
 * \section Handshake Integrity
 * 
 * Used to protect against man in the middle.
 * 
 * - Usually SHA, SHA-256 or SHA-384
 */