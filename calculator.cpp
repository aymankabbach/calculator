#include <iostream>
using namespace std;

class clsCalculator
{
private:
    float _result=0;
    float _LastNumber=0;

    void set_LastNumber(float number)
    {
        _LastNumber=number;
    }
    void set_result(int operation_number)
    {
        enum enOperations {Add=1,Subtract=2,Multiply=3,Divide=4};
        switch (operation_number)
        { 
            case Add:
                _result+=_LastNumber;
                break;
            case Subtract:
                _result-=_LastNumber;
                break;
            case Multiply:
                _result*=_LastNumber;
                break;
            case Divide:
                if (_LastNumber==0)
                {
                    cout<<"error, you can't divide by 0"<<endl;
                    break;
                }
                else
                {
                    _result=_result/_LastNumber;
                    break;
                }
        }    
    }
    float get_result()
    {
        return _result;
    }
    float get_LastNumber()
    {
        return _LastNumber;
    }
public:
    void Adding(float number)
    {
        set_LastNumber(number);
        set_result(1);
        cout<<"the result after adding "<<get_LastNumber()<<" is "<<get_result()<<endl;
    }
    void Subtract(float number)
    {
        set_LastNumber(number);
        set_result(2);
        cout<<"the result after subtracting "<<get_LastNumber()<<" is "<<get_result()<<endl;
    }
    void Multiply(float number)
    {
        set_LastNumber(number);
        set_result(3);
        cout<<"the result after Multiplying "<<get_LastNumber()<<" is "<<get_result()<<endl;
    }
    void Diving(float number)
    {
        set_LastNumber(number);
        set_result(4);
        if (number!=0)
        {
            cout<<"the result after Dividing "<<get_LastNumber()<<" is "<<get_result()<<endl;
        }
    }
};
int main()
{ 
    clsCalculator Calculator;
    system("pause>0");
    return 0;
}