/* ----------------------------------------------------------------------   
* Copyright (C) 2010-2012 ARM Limited. All rights reserved.   
*   
* $Date:        17. January 2013  
* $Revision: 	V1.4.0   
*   
* Project: 	    CMSIS DSP Library   
* Title:	     	arm_fir_data.c
*   
* Description:	 Data file used for example code
*   
* Target Processor: Cortex-M4/Cortex-M3/Cortex-M0
*  
* Redistribution and use in source and binary forms, with or without 
* modification, are permitted provided that the following conditions
* are met:
*   - Redistributions of source code must retain the above copyright
*     notice, this list of conditions and the following disclaimer.
*   - Redistributions in binary form must reproduce the above copyright
*     notice, this list of conditions and the following disclaimer in
*     the documentation and/or other materials provided with the 
*     distribution.
*   - Neither the name of ARM LIMITED nor the names of its contributors
*     may be used to endorse or promote products derived from this
*     software without specific prior written permission.
*
* THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
* "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
* LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
* FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE 
* COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
* INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
* BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
* LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
* CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
* LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
* ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
* POSSIBILITY OF SUCH DAMAGE.  
 * -------------------------------------------------------------------- */

#include "arm_math.h"

/* ----------------------------------------------------------------------
** Test input signal contains 1000Hz + 15000 Hz
** ------------------------------------------------------------------- */

float32_t testInput_f32_1kHz_15kHz[30] =
{
 13.000000,13.000000,207.000000,926.000000,-146.000000,-582.000000,-462.000000,-90.000000,-351.000000,
-177.000000,706.000000,329.000000,-262.000000,-86.000000,-114.000000,426.000000,31.000000,-14.000000,-38.000000,-118.000000,-86.000000,
-146.000000,-21.000000,122.000000,47.000000,-732.000000,43.000000,297.000000,108.000000,142.000000
};

float32_t refOutput[30] = 
{
    -0.0237,-0.0443,-0.3979,-1.9683,-1.0513,2.2739,6.9728,9.3752,4.6804,-11.2526,-33.6460,-42.7915,-17.2236,50.4173,142.7958,215.0753,219.2810,130.6817,-27.8202,-191.6247,-287.7593,-274.9356,-166.8447,-21.0926,96.4890,149.0311,137.9463,96.3578,57.5317,34.2024
};
