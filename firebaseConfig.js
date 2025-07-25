// Import the functions you need from the SDKs you need

import { initializeApp } from "firebase/app";

import { getAnalytics } from "firebase/analytics";

// TODO: Add SDKs for Firebase products that you want to use

// https://firebase.google.com/docs/web/setup#available-libraries


// Your web app's Firebase configuration

// For Firebase JS SDK v7.20.0 and later, measurementId is optional

const firebaseConfig = {

  apiKey: "AIzaSyC43l59jRoJ0PqSNhjmO3LR-kaxIBTxtVc",

  authDomain: "investimento-avan.firebaseapp.com",

  projectId: "investimento-avan",

  storageBucket: "investimento-avan.firebasestorage.app",

  messagingSenderId: "871469315884",

  appId: "1:871469315884:web:5aef92ecc40f79fd679e89",

  measurementId: "G-W952524979"

};


// Initialize Firebase

const app = initializeApp(firebaseConfig);

const analytics = getAnalytics(app);
