#include <iostream>
#include <string>

using namespace std;

class UAV{
    public:
        string name = "";
        bool is_landing = false;
        bool is_takeoff = false;

    bool takeoff(){
        return false;
    }
};