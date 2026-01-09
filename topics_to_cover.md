# Topics to Cover – REST E-Commerce API

This document outlines the core concepts studied and used while developing the REST-based E-Commerce API. 

***
## 1. JSON (JavaScript Object Notation)
IT is a lightweight data-interchange format which represents data in a key-value pair structure. This format is highly structured and readable, making it ideal for transmitting data through an api.

## 2. JWT and Session Management
A session is a server-side record that maintains a user’s authenticated state across multiple requests by associating a unique token with their identity and expiration time.

A JWT is a signed, URL-safe token consisting of a header, payload, and signature, used to securely transmit user identity and claims between parties, with built-in verification to prevent tampering.

## 3. Web Services
Web services are web APIs that allow apps to share data and work together through internet, no matter the platform or language.

## 4. API: REST and RPC
### REST (Representational State Transfer)
- Resource-based
- Uses HTTP methods (GET, POST, PUT, DELETE)
- Stateless
- Uses URLs to represent resources

### RPC (Remote Procedure Call)
- Action-based
- Calls methods/functions directly
- Less flexible than REST for web APIs

This project uses REST architecture.

## 5. Various HTTP Methods in RESTful API
RESTful APIs use standard HTTP methods to interact with resources

  -GET: Retrieve data from the server (e.g., get user details). safe , idemponent
  -POST: Send data to the server to create a new resource (e.g., add a new user). not safe , not idemponent
  -PUT: Update an existing resource with new data (e.g., update user information). not safe , idemponent
  -DELETE: Remove a resource from the server (e.g., delete a user). not safe , idemponent
  -PATCH: Apply partial updates to a resource (e.g., update only one field of user details). not   safe , not idemponent

## 6. Status Code in restful api:
A numerical code that indicates the result of the request (e.g., 200 for success, 404 for not found, 500 for server error).

## 7. Headers in restful api
HTTP headers carry metadata about requests and responses, including Authorization, Content-Type, Accept, Cache-Control, Custom headers.

## 8. Endpoints
Endpoints are URLs representing resources

## 9. Software Design Principles
### DRY (Don’t Repeat Yourself)
Avoid duplicating code.
Used by:
- Creating service layers
- Reusing common utility functions

### SOLID Principles
- **S**ingle Responsibility
- **O**pen/Closed principle
- **L**iskov Substitution principle
- **I**nterface Segregation principle
- **D**ependency Inversion principle

## 10. API Client – Insomnia
Insomnia is an API testing tool.
Used for:
- Sending HTTP requests
- Testing authentication
- Debugging API responses


## 11. SQLAlchemy
SQLAlchemy is a Python library that helps you work with databases more easily.
It is an ORM (Object Relational Mapper).
Used for:
- Database modeling
- Querying data using Python objects
- Managing database relationships

## 12. Serialization – Marshmallow
Marshmallow is used for:
- **Serialization**: Convert SQLAlchemy models (e.g., `Product`, `User`) into JSON responses.
    
- **Deserialization**: Convert incoming JSON payloads into Python objects or ORM models.
    
- **Validation**: Ensure incoming data meets requirements (e.g., price must be positive, email must be valid).
Marshmallow is built around schemas, A `Schema` defines **rules for translating Python objects ↔ dictionaries/JSON**.

## 13. Date and Time with Timezone
-In programming (especially Python), there are two types of datetime objects:

  1.Naive Datetime: A date/time with no timezone information (e.g., "Jan 1st, 2024, 10:00 AM"). The computer doesn't know if this is 10:00 AM in New York or Mumbai. This is dangerous for global apps.

  2.Aware Datetime: A date/time that includes an offset from UTC (e.g., "Jan 1st, 2024, 10:00 AM +05:30"). The computer knows exactly where this sits on the global timeline.

-**UTC (Coordinated Universal Time)** is the primary time standard by which the world regulates clocks and time. It is not a timezone itself, but the "Zero point."
-**DST (Daylight Saving Time)** is the practice of advancing clocks (usually by 1 hour) during warmer months so that darkness falls at a later clock time.
-**Unix Timestamp** is the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.

