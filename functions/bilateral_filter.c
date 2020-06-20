#include <stdio.h>
#include <math.h>

int processing(int arr[5][5]){
    int center_value = arr[2][2];
    double bilateral_filter[5][5];
    int i, j;

    int gaussian_filter[5][5] = {
        {1, 4, 6, 4, 1}, {4, 16, 24, 16, 4}, 
        {6, 24, 36, 24, 6}, {4, 16, 24, 16, 4}, 
        {1, 4, 6, 4, 1}
    };

    int sum = 0;
    for (i = 0; i < 5; i++)
        for (j = 0; j < 5; j++){
            double weight = exp(- pow(center_value - arr[i][j], 2) / 2);
            bilateral_filter[i][j] = gaussian_filter[i][j] * weight;
            sum += bilateral_filter[i][j];
        }

    double value = 0;
    for (i = 0; i < 5; i++)
        for (j = 0; j < 5; j++){
            value += bilateral_filter[i][j] * arr[i][j] / sum;
        }

    int result = (int)value;

    return result;
}