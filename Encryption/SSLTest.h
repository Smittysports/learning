/** \page SSL_Encryption SSL Encryption
 * 
 * \section Acronyms
 * - SSL (Secure Socket Layer)
 * - TLS (Transport Layer Security)
 * 
 * \section Overview
 * TBD
 * 
 * \section Encryption Algorithms
 * - RSA
 * - Diffie Hellman
 * - ECDHE
 * - 3DES
 * - AES
 * - ChaCha20
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
 * 
 * \section Negotiation
 * TLS (Transport Layer Security) is the trasnport protocol used for secure communication. It is referred
 * to as SSL because they were the original protocols used by Netscape Navigator. TLS evolved from SSL, which
 * is no longer safe.
 * 
 * TLS 1.2 and 1.3 are the most recent as of 9/19/2023. TLS 1.3 is more secure and utilize less overhead in
 * the handshake.
 */