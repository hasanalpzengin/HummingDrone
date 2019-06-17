#include "UAV.h"
#include <iostream>
#include <string>

using namespace std;

class Drone : public UAV{
    //constructor
    public:
        Drone(string new_name){
            this->name = new_name;
        }

        bool takeoff(){
            if(this->is_landing){
                return false;
            }
            //ternary
            this->is_takeoff = this->is_takeoff ? false : true;
            return is_takeoff;
        }
};