/*
 * Copyright (c) 2014-2020 Arm Limited and affiliates.
 * SPDX-License-Identifier: Apache-2.0
 */

#include "mbed.h"

// Adjust pin name to your board specification.
// You can use LED1/LED2/LED3/LED4 if any is connected to PWM capable pin,
// or use any PWM capable pin, and see generated signal on logical analyzer.
PwmOut led(PWM_OUT);
bool adjust = false;
bool flip = false;
float dutycycle=1.0f;
InterruptIn button(BUTTON1);

void bp(){

    adjust=!adjust;
}

int main()
{
    // specify period first
    led.period(0.001f); 
         // 4 second period
    button.fall(&bp);
    button.rise(&bp);
    while(1){
        while(adjust){
            if (flip){
                // dutycycle += 0.000005;
                dutycycle /= 0.9999;
                led.write(dutycycle);
                if(dutycycle>1){
                    flip=false;
                }
            }
            if(!flip){
                dutycycle *= 0.9999;
                led.write(dutycycle);
                if (dutycycle<0.001){
                    flip=true;
                }
            
            }     
        } 
    }
     
     
    
    //led = 0.5f;          // shorthand for led.write()
    //led.pulsewidth(2);   // alternative to led.write, set duty cycle time in seconds
    // while (1);
}
