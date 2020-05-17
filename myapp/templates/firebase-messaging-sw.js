// Give the service worker access to Firebase Messaging.
// Note that you can only use Firebase Messaging here, other Firebase libraries
// are not available in the service worker.
importScripts('https://www.gstatic.com/firebasejs/7.12.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/7.7.0/firebase-messaging.js');

// Initialize the Firebase app in the service worker by passing in
// your app's Firebase config object.
// https://firebase.google.com/docs/web/setup#config-object
var firebaseConfig = {
    apiKey: "AIzaSyAtF3TNqqK82JChMfS6M6BDMOzsNeH8HO0",
    authDomain: "fcmproject-a5dda.firebaseapp.com",
    databaseURL: "https://fcmproject-a5dda.firebaseio.com",
    projectId: "fcmproject-a5dda",
    storageBucket: "fcmproject-a5dda.appspot.com",
    messagingSenderId: "501828232429",
    appId: "1:501828232429:web:eae7a1faee949c4ed2d8e4"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
// Retrieve an instance of Firebase Messaging so that it can handle background
// messages.
const messaging = firebase.messaging();