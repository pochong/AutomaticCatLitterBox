/* ========================================
 *
 * Copyright YOUR COMPANY, THE YEAR
 * All Rights Reserved
 * UNPUBLISHED, LICENSED SOFTWARE.
 *
 * CONFIDENTIAL AND PROPRIETARY INFORMATION
 * WHICH IS THE PROPERTY OF your company.
 *
 * ========================================
*/
#include "project.h"
int adc = 0;
uint8 txstat = 0;
CY_ISR(Tx){
    txstat = UART_1_ReadTxStatus();
    if(txstat&UART_1_TX_STS_FIFO_EMPTY) {
        UART_1_WriteTxData(adc);
    }
    Timer_1_ReadStatusRegister();
}
int main(void)
{
    CyGlobalIntEnable; /* Enable global interrupts. */
    UART_1_ClearRxBuffer();
    UART_1_ClearTxBuffer();
    ADC_DelSig_1_Start();
    ADC_DelSig_1_StartConvert();
    isr_1_StartEx(Tx);
    UART_1_Start();
    Timer_1_Start();
    
    /* Place your initialization/startup code here (e.g. MyInst_Start()) */

    for(;;)
    {
        /* Place your application code here. */
        adc = ADC_DelSig_1_Read16();
        if(adc<0) adc = 0;
        if(adc>255) adc = 255;
    }
}

/* [] END OF FILE */
