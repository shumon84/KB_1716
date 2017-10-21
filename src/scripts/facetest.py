import httplib, urllib, base64, json
import choice
import sys
import cv2

args = sys.argv

###############################################
#### Update or verify the following values. ###
###############################################

# Replace the subscription_key string value with your valid subscription key.
subscription_key = 'f129ff39951f44389bb7ce898ec23c14'

# Replace or verify the region.
#
# You must use the same region in your REST API call as you used to obtain your subscription keys.
# For example, if you obtained your subscription keys from the westus region, replace 
# "westcentralus" in the URI below with "westus".
#
# NOTE: Free trial subscription keys are generated in the westcentralus region, so if you are using
# a free trial subscription key, you should not need to change this region.
uri_base = 'westcentralus.api.cognitive.microsoft.com'

# Request headers.
headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

# Request parameters.
params = urllib.urlencode({
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
})

# The URL of a JPEG image to analyze.
#body = "{'url':'http:q//www.aflo.com/creative/people/img/mainImg.jpg'}"
body = open(args[1],'rb')

img = cv2.imread(args[1] )

try:
    # Execute the REST API call and get the response.
    conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()

    # 'data' contains the JSON data. The following formats the JSON data for display.
    parsed = json.loads(data)
    if len(parsed) == 2:
        A = {'x':parsed[0]['faceRectangle']['left']}
        A['anger'] = parsed[0]['emotion']['anger']
        A['contempt'] = parsed[0]['emotion']['comtempt']
        A['disgust'] = parsed[0]['emotion']['disgust']
        A['fear'] = parsed[0]['emotion']['fear']
        A['happiness'] = parsed[0]['emotion']['happiness']
        A['neutral'] = parsed[0]['emotion']['neutral']
        A['sadness'] = parsed[0]['emotion']['sadness']
        A['surprise'] = parsed[0]['emotion']['surprise']
        A['exposure'] = parsed[0]['exposure']['value']

        B = {'x':parsed[1]['faceRectangle']['left']}
        B['anger'] = parsed[1]['emotion']['anger']
        B['contempt'] = parsed[1]['emotion']['comtempt']
        B['disgust'] = parsed[1]['emotion']['disgust']
        B['fear'] = parsed[1]['emotion']['fear']
        B['happiness'] = parsed[1]['emotion']['happiness']
        B['neutral'] = parsed[1]['emotion']['neutral']
        B['sadness'] = parsed[1]['emotion']['sadness']
        B['surprise'] = parsed[1]['emotion']['surprise']
        B['exposure'] = parsed[1]['exposure']['value']

        ret = choice.choice(A, B)
    else:
        print('ERROR')
    if len(parsed) < 2:
            ret = -2
        else:
            ret = -1
    
    conn.close()

    return ret

except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
####################################
