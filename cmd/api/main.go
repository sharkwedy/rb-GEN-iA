package main

import (
	"net/http"
	"github.com/gorilla/mux"
)

func main() {
	r := mux.NewRouter()

	r.HandleFunc("/pessoas", CreatePerson).Methods("POST")
	r.HandleFunc("/pessoas/{id}", GetPersonByID).Methods("GET")
	r.HandleFunc("/pessoas", SearchPeople).Queries("t", "{termo}").Methods("GET")
	r.HandleFunc("/contagem-pessoas", CountPeople).Methods("GET")

	http.ListenAndServe(":8080", r)
}

func CreatePerson(w http.ResponseWriter, r *http.Request) {
	// Implement creation logic here
}

func GetPersonByID(w http.ResponseWriter, r *http.Request) {
	// Implement get logic here
}

func SearchPeople(w http.ResponseWriter, r *http.Request) {
	// Implement search logic here
}

func CountPeople(w http.ResponseWriter, r *http.Request) {
	// Implement count logic here
}