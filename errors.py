
def init_errors(app):

    @app.errorhandler(404)
    def raise_404(error):
        return "Add a sexy 404 page here."
