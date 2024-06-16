package domain

import "time"

type Person struct {
    ID        string    `json:"id" validate:"required,uuid"`
    FirstName string    `json:"first_name" validate:"required"`
    LastName  string    `json:"last_name" validate:"required"`
    Email     string    `json:"email" validate:"required,email"`
    Birthdate time.Time `json:"birthdate" validate:"required"`
    Address   *Address  `json:"address,omitempty"`
}

type Address struct {
    Street  string `json:"street" validate:"required"`
    City    string `json:"city" validate:"required"`
    State   string `json:"state" validate:"required"`
    ZipCode string `json:"zip_code" validate:"required"`
}