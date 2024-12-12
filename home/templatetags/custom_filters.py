from django import template

register = template.Library()

@register.filter
def contains(palavra, substring):
    return str(substring).lower() in str(palavra).lower()





"""

                            <div class="col">
                                <div class="bg-white w-100">
                                    <div class="box border-1 position-relative mx-auto" style="width: 300px;height: 300px;">
                                        <img id="frentex" src="{% static 'home/img/reais/frente-preta.png' %}" alt=""
                                            class="w-100 position-absolute top-0 start-0" style="z-index: 1;">
                                        <img id="alcax" src="{% static 'home/img/reais/alca-preta.png' %}" alt=""
                                            class="w-100 position-absolute top-0 start-0" style="z-index: 0;">
                                    </div>
                                </div>
                            </div>

"""