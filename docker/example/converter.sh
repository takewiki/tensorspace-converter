#!/usr/bin/env bash
tensorspacejs_converter \
    --input_model_from="keras" \
    --input_model_format="topology_weights_combined" \
    --output_layer_names='reshape_1,Conv2D_1,MaxPooling2D_1,Conv2D_2,MaxPooling2D_2,flatten_1,Dense_1,Dense_2,Softmax' \
    ./input/keras_model.h5 \
    ./output