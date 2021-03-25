#include "NumeroImaginario.h"
#include <cmath>

using namespace ImagComp;

NumeroImaginario::NumeroImaginario(double a , double b){
    this->Data.a= a;
    this->Data.b= b;
}

NumeroImaginario::~NumeroImaginario(){
    
}

struct BaseData NumeroImaginario::GetValueCart(){
    return this->Data;
}

struct BaseData NumeroImaginario::GetValuePolar(){
    struct BaseData toReturn;
    toReturn.a = sqrt(this->Data.a*this->Data.a + this->Data.b*this->Data.b);
    toReturn.b = atan(this->Data.b/this->Data.b);
    return toReturn;
};

NumeroImaginario* NumeroImaginario::operator+(NumeroImaginario num){
    struct BaseData val = num.GetValueCart();
    return new NumeroImaginario(
        this->Data.a+val.a,
        this->Data.b+val.b);
};

NumeroImaginario* NumeroImaginario::operator-(NumeroImaginario num){
    struct BaseData val = num.GetValueCart();
    return new NumeroImaginario(
        this->Data.a-val.a,
        this->Data.b-val.b);
};

NumeroImaginario* NumeroImaginario::operator*(NumeroImaginario num){
    struct BaseData val = num.GetValueCart();
    return new NumeroImaginario(
        this->Data.a*val.a-this->Data.b*val.b,
        this->Data.a*val.b+this->Data.b*val.a);
};

NumeroImaginario* NumeroImaginario::operator/(NumeroImaginario num){
    struct BaseData val = num.GetValueCart();
    double d = val.a*val.a+val.b*val.b; 
    return new NumeroImaginario(
        (this->Data.a*val.a+this->Data.b*val.b),
        this->Data.b*val.a-this->Data.a+val.b);
};
