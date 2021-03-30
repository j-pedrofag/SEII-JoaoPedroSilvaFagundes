#include <iostream>
#include "NumeroImaginario.h"

using namespace std;
using namespace ImagComp;

int main(){
    NumeroImaginario x(1,1),y(2,2);
    cout << "Os numeros imaginario para este exemplo sao: 1 +1i e 2 + 2i \n" ;
    cout << "A soma e: " ;
    NumeroImaginario* z = x+y;
    cout<< z->GetValueCart().a << " " << z->GetValueCart().b << endl;
    cout << "A subtracao e: ";
    z = x-y;
    cout<< z->GetValueCart().a << " " << z->GetValueCart().b << endl;
    cout << "A divisao e: ";
    z = x/y;
    cout<< z->GetValueCart().a << " " << z->GetValueCart().b << endl;
    cout << "A multiplicacao e: ";
    z = x*y;
    cout<< z->GetValueCart().a << " " << z->GetValueCart().b << endl;
    cout << "A forma da multiplicacao polar e: " ;
    cout<< z->GetValuePolar().a << " " << z->GetValuePolar().b << endl;
	
    return 0;
}
