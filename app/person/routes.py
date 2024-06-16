class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)

@app.route('/persons', methods=['POST'])
def create_person():
    data = request.get_json()
    new_person = Person(name=data['name'], age=data['age'])
    db.session.add(newag_person)
    db.session.commit()
    return jsonify({'message': 'Person created successfully'}), 201

@app.route('/persons/<int:id>', methods=['GET'])
def get_person(id):
    person = Person.query.get_or_404(id)
    return jsonify({'name': person.name, 'age': person.age})

@app.route('/persons/<int:id>', methods=['PUT'])
def update_person(id):
    person = Person.query.get_or_404(id)
    data = request.get_json()
    person.name = data['name']
    person.age = data['age']
    db.session.commit()
    return jsonify({'message': 'Person updated successfully'})

@app.route('/persons/<int:id>', methods=['DELETE'])
def delete_person(id):
    person = Person.query.get_or_404(id)
    db.session.delete(person)
    db.session.commit()
    return jsonify({'message': 'Person deleted successfully'})