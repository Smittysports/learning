#include <string>

/** \page Networking
 *
 * Examples of networking protocls are HTTP, TCP-IP, UDP
 * - HTTP (Hypertext transfer protocol)
 * - TCP (Transmission control protocol)
 * - UDP (User datagram protocol)
 * 
 * Web browsers do not support communication with TCP-IP or UDP because
 * of security issues.
 * 
 * HTTP is the main protocol for Web browsers.
 * - Javascript can send HTTP requests using
 *   - AJAX
 *   - jQuery
 *   - fetch
 *   - etc...
 * 
 * For this application, I am using jQuery. The jQuery I use looks like this:
 *   fetch('http://192.168.1.11:47808') 
 *     .then(function(response) { 
 *       console.log("Got it");
 *     }, function(e) {
 *       console.log("Error");
 *   })
 * 
 * The jQuery expects the response to be similar to this:
 *   char htmlResponse[512] = "HTTP/1.1 200 OK";
 */

/**
 * Contains the networking thread and methods for creating TCP and UDP listeners.
*/
class Networking
{
public:
  /** Constructor */
  Networking() : m_ipAddress("0.0.0.0"){};

  ~Networking() = default;

  void createConnection();

  constexpr static const unsigned short DEFAULT_BUFLEN = 512;
  constexpr static const unsigned short DEFAULT_PORT = 47808;

private:
  std::string m_ipAddress;

  int udpThread();

  int tcpThread();
};
