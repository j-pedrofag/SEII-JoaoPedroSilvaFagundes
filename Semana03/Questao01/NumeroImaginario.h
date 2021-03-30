namespace ImagComp{

struct BaseData{
    double a;
    double b;
};

class NumeroImaginario
{
private:
    struct BaseData Data;
public:
    NumeroImaginario(double a, double b);
    ~NumeroImaginario();
    struct BaseData GetValueCart();
    struct BaseData GetValuePolar();
    NumeroImaginario* operator+(NumeroImaginario by);
    NumeroImaginario* operator-(NumeroImaginario by);
    NumeroImaginario* operator*(NumeroImaginario by);
    NumeroImaginario* operator/(NumeroImaginario by);
};

}
