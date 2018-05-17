#!/usr/bin/env python3

import boto3

if __name__ == "__main__":

    imageFile='IMG_0014.PNG'
    client=boto3.client('rekognition','eu-west-1')
   
    with open(imageFile, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})
        
    print('Detected labels in ' + imageFile)    
    for label in response['Labels']:
        print (label['Name'] + ' : ' + str(label['Confidence']))

    print('Done...')

