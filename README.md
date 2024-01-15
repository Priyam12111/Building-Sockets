# Building-Sockets
## There are some rules for ngrok 
1. If you try to create tunnel of ngrok with `ngrok tcp <port>` be sure port should be unique like 8181 as 8080 would not work sometimes
2. Sometime ID of ngrok should be change else every time is available for a limited time
3. Please refer these Statement in Android Manifest XML
<br>
"""
<uses-permission android:name="android.permission.READ_SMS"/>`
`<uses-permission android:name="android.permission.RECEIVE_SMS"/>`
`<uses-permission android:name="android.permission.INTERNET" />`
"""
## Rest you will get it by see the code
