from flask import Flask, render_template,request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_restful import Api
  

app = Flask(__name__, template_folder='template')
api = Api(app)
#configuração com banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud4.db'
db = SQLAlchemy(app)

from app.models.products import Products
with app.app_context():
    db.create_all()

from app.view.reso_products import Index, ProductCreate, ProductUpdate, ProductDelete
api.add_resource(Index, '/') #como se fosse a rota, so que com a chamada da api
api.add_resource(ProductCreate, '/criar')
api.add_resource(ProductUpdate, '/atualizar')
api.add_resource(ProductDelete, '/delete')



@app.route("/")
def Index():
    produtos = Products.query.all()
    return render_template('index.html', produtos=produtos)


# Rota para excluir um produto
@app.route('/delete/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    
    return jsonify({'message': f'Produto com ID {product_id} excluído com sucesso'})





if __name__ == '__main__':
    app.run(debug=True)