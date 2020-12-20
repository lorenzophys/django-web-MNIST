from django.views.generic import TemplateView
from django.http import JsonResponse

from .helpers.image_preprocessing import ImageProcessor
from .helpers.tensorflow_model import TensorflowModel


class HomePageView(TemplateView):
    template_name = 'routes/home.html'
    tf_model = TensorflowModel('./web_MNIST/tf_model/MNIST_digits_CNN_model.h5')

    def post(self, request, **kwargs):
        image_url = request.POST.get('imgBase64')

        processor = ImageProcessor(image_url)
        prepared_image = processor.prepare_image_for_evaluation()

        prediction = self.tf_model.predict(prepared_image)
        response = {'prediction': str(prediction)}

        return JsonResponse(response)
