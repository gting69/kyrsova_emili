from odoo.tests.common import TransactionCase


class TestCoworking(TransactionCase):

    def setUp(self):
        super(TestCoworking, self).setUp()

        self.room = self.env['coworking.room'].create({
            'name': 'Test Room',
            'capacity': 10
        })

        self.desk = self.env['coworking.desk'].create({
            'name': 'Test Desk',
            'room_id': self.room.id
        })

        self.rate = self.env['coworking.rate'].create({
            'name': 'Test Rate',
            'price': 100.0
        })

        self.service = self.env['coworking.service'].create({
            'name': 'Test Service',
            'cost': 50.0
        })

    def test_01_room_creation(self):
        """Тест моделі Room: перевірка створення та активності"""
        self.assertEqual(self.room.name, 'Test Room')
        self.assertTrue(self.room.active)

    def test_02_desk_link(self):
        """Тест моделі Desk: перевірка зв'язку з кімнатою"""
        self.assertEqual(self.desk.room_id.id, self.room.id)

    def test_03_rate_price(self):
        """Тест моделі Rate: перевірка вартості"""
        self.assertEqual(self.rate.price, 100.0)

    def test_04_service_cost(self):
        """Тест моделі Service: перевірка ціни послуги"""
        self.assertEqual(self.service.cost, 50.0)

    def test_05_booking_flow(self):
        """Тест моделі Booking: створення бронювання через код"""
        booking = self.env['coworking.booking'].create({
            'partner_id': self.env.ref('base.partner_admin').id,
            'room_id': self.room.id,
            'start_date': '2026-02-01 10:00:00',
            'end_date': '2026-02-01 12:00:00',
        })

        self.assertEqual(booking.state, 'draft')
        booking.action_confirm()
        self.assertEqual(booking.state, 'confirmed')
