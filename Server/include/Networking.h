class Networking
{
  public:
    Networking() = default;

    ~Networking() = default;

    void createConnection();

  private:
    void AcceptThread();
};
