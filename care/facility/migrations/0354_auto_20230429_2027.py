# Generated by Django 2.2.11 on 2023-04-17 04:06

from django.db import migrations

from care.facility.models.prescription import PrescriptionType


def migrate_prescriptions(apps, schema_editor):
    PatientConsultation = apps.get_model('facility', 'PatientConsultation')
    Prescription = apps.get_model('facility', 'Prescription')
    DailyRound = apps.get_model('facility', 'DailyRound')

    for consultation in PatientConsultation.objects.all():
        for advice in consultation.discharge_advice:
            Prescription.objects.create(
                frequency=advice['dosage'].upper(),
                dosage=advice['dosage_new'],
                medicine=advice['medicine'],
                days=advice['days'],
                notes=advice['notes'],
                route=advice['route'].upper(),
                consultation=consultation,
                is_prn=False,  # TODO : Why is this true
                prescribed_by=consultation.created_by,
                is_migrated=True,
                prescription_type=PrescriptionType.REGULAR.value,
                created_date=consultation.modified_date,
                modified_date=consultation.modified_date,
            )
        for advice in consultation.prn_prescription:
            Prescription.objects.create(
                medicine=advice['medicine'],
                dosage=advice['dosage'],
                indicator=advice['indicator'],
                max_dosage=advice['max_dosage'],
                min_hours_between_doses=advice['min_time'],
                route=advice['route'].upper(),
                consultation=consultation,
                is_prn=True,
                prescribed_by=consultation.created_by,
                is_migrated=True,
                prescription_type=PrescriptionType.REGULAR.value,
                created_date=consultation.modified_date,
                modified_date=consultation.modified_date,
            )
        for advice in consultation.discharge_prescription:
            Prescription.objects.create(
                frequency=advice['dosage'].upper(),
                dosage=advice['dosage_new'],
                medicine=advice['medicine'],
                days=advice['days'],
                notes=advice['notes'],
                route=advice['route'].upper(),
                consultation=consultation,
                is_prn=False,  # TODO : Why is this true
                prescribed_by=consultation.created_by,
                is_migrated=True,
                prescription_type=PrescriptionType.DISCHARGE.value,
                created_date=consultation.modified_date,
                modified_date=consultation.modified_date,
            )
        for advice in consultation.discharge_prn_prescription:
            Prescription.objects.create(
                medicine=advice['medicine'],
                dosage=advice['dosage'],
                indicator=advice['indicator'],
                max_dosage=advice['max_dosage'],
                min_hours_between_doses=advice['min_time'],
                route=advice['route'].upper(),
                consultation=consultation,
                is_prn=True,
                prescribed_by=consultation.created_by,
                is_migrated=True,
                prescription_type=PrescriptionType.DISCHARGE.value,
                created_date=consultation.modified_date,
                modified_date=consultation.modified_date,
            )
        daily_round_objects = DailyRound.objects.filter(consultation=consultation).order_by("id")
        prescriptions = []
        for daily_round in daily_round_objects:
            if daily_round.medication_given:
                prescriptions.append([daily_round.medication_given, daily_round.created_date])
        medicines_given = []
        current_medicines = {}
        updates = 0
        for prescription in prescriptions:
            for advice in prescription[0]:
                key = str(advice['medicine'] or "") + str(advice['dosage'] or "") + str(
                    advice.get('indicator') or "") + str(advice.get('max_dosage') or "") + str(advice.get('min_time') or "")
                if key not in current_medicines:
                    current_medicines[key] = { "advice":  advice, "update_count": 0 }
                current_medicines[key]["update_count"] += 1
            updates += 1
            for key in list(current_medicines.keys()):
                if current_medicines[key] != updates:
                    advice = current_medicines.pop(key)["advice"]
                    medicines_given.append(Prescription(
                        medicine=advice['medicine'],
                        dosage=advice['dosage'],
                        indicator=advice.get('indicator'),
                        max_dosage=advice.get('max_dosage'),
                        min_hours_between_doses=advice.get('min_time'),
                        route=advice['route'].upper(),
                        consultation=consultation,
                        is_prn=False,
                        prescribed_by=consultation.created_by,
                        is_migrated=True,
                        prescription_type=PrescriptionType.REGULAR.value,
                        discontinued=True,
                        created_date=prescription[1]
                    ))
            for key in list(current_medicines.keys()):
                advice = current_medicines.pop(key)
                medicines_given.append(Prescription(
                    medicine=advice['medicine'],
                    dosage=advice['dosage'],
                    indicator=advice.get('indicator'),
                    max_dosage=advice.get('max_dosage'),
                    min_hours_between_doses=advice.get('min_time'),
                    route=advice['route'].upper(),
                    consultation=consultation,
                    is_prn=False,
                    prescribed_by=consultation.created_by,
                    is_migrated=True,
                    prescription_type=PrescriptionType.REGULAR.value,
                    discontinued=True,
                    created_date=prescription[1]
                ))
    # Look at all daily round objects under this consultation
    # Fetch all prescriptions for that patient
    # For patients with multiple prescriptions :
    #   Start from the first prescription item and calculate how long it continued for
    #   Discontinued date is the first date when the prescription was removed or the discharge date if present
    #   Perform this for all prescriptions


class Migration(migrations.Migration):
    dependencies = [
        ('facility', '0353_auto_20230429_2026'),
    ]

    operations = [
        migrations.RunPython(migrate_prescriptions),
    ]