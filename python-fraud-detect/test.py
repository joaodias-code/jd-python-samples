import events
import integrator

#detectar eventos fake
event_name = 'Xpower Force funciona Preço boleto farmacia tomar onde comprar XpowerForce?'
event_code = 71

print(events.detect_fake(event_name))

#if gofree_events.detect_fake(event_name):
#    gofree_integrator.suspender_evento(event_code)

