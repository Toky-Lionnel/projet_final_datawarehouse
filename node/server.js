const express = require('express');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());

// ========================
// 1. Taux de change
// ========================
app.get('/api/exchange-rates', (req, res) => {
  const rates = {
    USD_EUR: 0.92,
    EUR_MGA: 4850,
    JPY_USD: 0.0067,
    USD_GBP: 0.79,
    EUR_GBP: 0.86,
    USD_JPY: 149.20,
    GBP_MGA: 5700,
    CNY_USD: 0.14,
    INR_USD: 0.012,
    KRW_USD: 0.00075,
    VND_USD: 0.000041,
    MYR_USD: 0.21
  };
  res.json(rates);
});

// ========================
// 2. Expéditions (shipments)
// Retourne une liste d'environ 20 expéditions simulées
// ========================
app.get('/api/shipments', (req, res) => {
  const shipments = [
    { shipment_id: 'SHP1001', order_id: 101, origin: 'Paris, France', destination: 'Berlin, Germany', status: 'delivered', delay_days: 0, shipping_cost_usd: 45.50, carrier: 'DHL' },
    { shipment_id: 'SHP1002', order_id: 102, origin: 'New York, USA', destination: 'Los Angeles, USA', status: 'delivered', delay_days: 2, shipping_cost_usd: 78.20, carrier: 'UPS' },
    { shipment_id: 'SHP1003', order_id: 103, origin: 'Tokyo, Japan', destination: 'Osaka, Japan', status: 'in_transit', delay_days: null, shipping_cost_usd: 32.00, carrier: 'Yamato' },
    { shipment_id: 'SHP1004', order_id: 104, origin: 'Shanghai, China', destination: 'Beijing, China', status: 'delivered', delay_days: 1, shipping_cost_usd: 28.90, carrier: 'SF Express' },
    { shipment_id: 'SHP1005', order_id: 105, origin: 'Mumbai, India', destination: 'Delhi, India', status: 'pending', delay_days: null, shipping_cost_usd: 15.75, carrier: 'DTDC' },
    { shipment_id: 'SHP1006', order_id: 106, origin: 'Seoul, South Korea', destination: 'Busan, South Korea', status: 'delivered', delay_days: 0, shipping_cost_usd: 22.30, carrier: 'CJ Logistics' },
    { shipment_id: 'SHP1007', order_id: 107, origin: 'Ho Chi Minh City, Vietnam', destination: 'Hanoi, Vietnam', status: 'delivered', delay_days: 3, shipping_cost_usd: 19.99, carrier: 'Viettel Post' },
    { shipment_id: 'SHP1008', order_id: 108, origin: 'Kuala Lumpur, Malaysia', destination: 'Penang, Malaysia', status: 'delivered', delay_days: 0, shipping_cost_usd: 12.50, carrier: 'Pos Malaysia' },
    { shipment_id: 'SHP1009', order_id: 109, origin: 'London, UK', destination: 'Manchester, UK', status: 'delivered', delay_days: 1, shipping_cost_usd: 35.00, carrier: 'Royal Mail' },
    { shipment_id: 'SHP1010', order_id: 110, origin: 'Madrid, Spain', destination: 'Barcelona, Spain', status: 'in_transit', delay_days: null, shipping_cost_usd: 41.25, carrier: 'Correos' },
    { shipment_id: 'SHP1011', order_id: 111, origin: 'Rome, Italy', destination: 'Milan, Italy', status: 'delivered', delay_days: 0, shipping_cost_usd: 38.60, carrier: 'Poste Italiane' },
    { shipment_id: 'SHP1012', order_id: 112, origin: 'Chicago, USA', destination: 'Houston, USA', status: 'delivered', delay_days: 5, shipping_cost_usd: 89.99, carrier: 'FedEx' },
    { shipment_id: 'SHP1013', order_id: 113, origin: 'San Francisco, USA', destination: 'Seattle, USA', status: 'delayed', delay_days: 7, shipping_cost_usd: 67.45, carrier: 'USPS' },
    { shipment_id: 'SHP1014', order_id: 114, origin: 'Sydney, Australia', destination: 'Melbourne, Australia', status: 'delivered', delay_days: 0, shipping_cost_usd: 55.00, carrier: 'Australia Post' },
    { shipment_id: 'SHP1015', order_id: 115, origin: 'Sao Paulo, Brazil', destination: 'Rio de Janeiro, Brazil', status: 'in_transit', delay_days: null, shipping_cost_usd: 48.90, carrier: 'Correios' },
    { shipment_id: 'SHP1016', order_id: 116, origin: 'Mexico City, Mexico', destination: 'Guadalajara, Mexico', status: 'delivered', delay_days: 2, shipping_cost_usd: 30.30, carrier: 'Estafeta' },
    { shipment_id: 'SHP1017', order_id: 117, origin: 'Toronto, Canada', destination: 'Vancouver, Canada', status: 'delivered', delay_days: 0, shipping_cost_usd: 72.10, carrier: 'Canada Post' },
    { shipment_id: 'SHP1018', order_id: 118, origin: 'Cairo, Egypt', destination: 'Alexandria, Egypt', status: 'pending', delay_days: null, shipping_cost_usd: 25.00, carrier: 'Egypt Post' },
    { shipment_id: 'SHP1019', order_id: 119, origin: 'Istanbul, Turkey', destination: 'Ankara, Turkey', status: 'delivered', delay_days: 1, shipping_cost_usd: 27.80, carrier: 'PTT' },
    { shipment_id: 'SHP1020', order_id: 120, origin: 'Moscow, Russia', destination: 'Saint Petersburg, Russia', status: 'delivered', delay_days: 4, shipping_cost_usd: 62.00, carrier: 'Russian Post' }
  ];
  res.json(shipments);
});

// ========================
// 3. Impact météo (weather-impact)
// Retourne une liste de 20 impacts météo sur les expéditions
// ========================
app.get('/api/weather-impact', (req, res) => {
  const impacts = [
    { region: 'Northern Europe', date: '2024-12-15', condition: 'Snowstorm', delay_risk: 'high', affected_shipments: 45 },
    { region: 'USA Midwest', date: '2024-12-18', condition: 'Heavy Rain', delay_risk: 'medium', affected_shipments: 23 },
    { region: 'Southeast Asia', date: '2024-12-20', condition: 'Typhoon', delay_risk: 'extreme', affected_shipments: 120 },
    { region: 'Japan', date: '2024-12-22', condition: 'Typhoon', delay_risk: 'high', affected_shipments: 67 },
    { region: 'India', date: '2024-12-25', condition: 'Fog', delay_risk: 'low', affected_shipments: 8 },
    { region: 'Australia', date: '2024-12-27', condition: 'Heatwave', delay_risk: 'medium', affected_shipments: 15 },
    { region: 'South America', date: '2024-12-28', condition: 'Flooding', delay_risk: 'high', affected_shipments: 34 },
    { region: 'Canada', date: '2024-12-29', condition: 'Blizzard', delay_risk: 'extreme', affected_shipments: 89 },
    { region: 'China', date: '2024-12-30', condition: 'Smog', delay_risk: 'low', affected_shipments: 12 },
    { region: 'Europe Central', date: '2025-01-02', condition: 'Storm', delay_risk: 'high', affected_shipments: 56 },
    { region: 'UK', date: '2025-01-05', condition: 'Storm', delay_risk: 'medium', affected_shipments: 41 },
    { region: 'Middle East', date: '2025-01-07', condition: 'Sandstorm', delay_risk: 'high', affected_shipments: 22 },
    { region: 'West Africa', date: '2025-01-10', condition: 'Heavy Rain', delay_risk: 'medium', affected_shipments: 18 },
    { region: 'Russia', date: '2025-01-12', condition: 'Extreme Cold', delay_risk: 'extreme', affected_shipments: 73 },
    { region: 'Mexico', date: '2025-01-14', condition: 'Hurricane', delay_risk: 'extreme', affected_shipments: 150 },
    { region: 'Scandinavia', date: '2025-01-16', condition: 'Ice Storm', delay_risk: 'high', affected_shipments: 37 },
    { region: 'Brazil', date: '2025-01-18', condition: 'Landslide', delay_risk: 'high', affected_shipments: 28 },
    { region: 'South Africa', date: '2025-01-20', condition: 'Heatwave', delay_risk: 'low', affected_shipments: 5 },
    { region: 'Korea', date: '2025-01-22', condition: 'Snow', delay_risk: 'medium', affected_shipments: 19 },
    { region: 'Vietnam', date: '2025-01-24', condition: 'Flooding', delay_risk: 'high', affected_shipments: 44 }
  ];
  res.json(impacts);
});

// ========================
// 4. Score fournisseur (supplier-score)
// Retourne une liste de scores de performance des fournisseurs
// ========================
app.get('/api/supplier-score', (req, res) => {
  const scores = [
    { supplier_id: 'SUP001', name: 'Fromages de France', country: 'France', on_time_delivery_rate: 98.5, quality_score: 9.2, cost_competitiveness: 8.5, overall_score: 8.9 },
    { supplier_id: 'SUP002', name: 'Bayerische Brauerei', country: 'Germany', on_time_delivery_rate: 95.0, quality_score: 8.9, cost_competitiveness: 8.0, overall_score: 8.4 },
    { supplier_id: 'SUP003', name: 'Pasta Italia SRL', country: 'Italy', on_time_delivery_rate: 92.3, quality_score: 9.0, cost_competitiveness: 7.8, overall_score: 8.2 },
    { supplier_id: 'SUP004', name: 'Iberico Ham Suppliers', country: 'Spain', on_time_delivery_rate: 88.7, quality_score: 9.5, cost_competitiveness: 6.5, overall_score: 8.0 },
    { supplier_id: 'SUP005', name: 'Tea & Biscuits UK', country: 'United Kingdom', on_time_delivery_rate: 97.1, quality_score: 8.7, cost_competitiveness: 7.9, overall_score: 8.5 },
    { supplier_id: 'SUP006', name: 'Vins de Bourgogne', country: 'France', on_time_delivery_rate: 96.4, quality_score: 9.3, cost_competitiveness: 7.5, overall_score: 8.7 },
    { supplier_id: 'SUP007', name: 'TechParts USA', country: 'USA', on_time_delivery_rate: 99.2, quality_score: 9.8, cost_competitiveness: 6.0, overall_score: 8.9 },
    { supplier_id: 'SUP008', name: 'Midwest Foods', country: 'USA', on_time_delivery_rate: 94.5, quality_score: 8.5, cost_competitiveness: 8.8, overall_score: 8.6 },
    { supplier_id: 'SUP009', name: 'Sony Electronics', country: 'Japan', on_time_delivery_rate: 100.0, quality_score: 9.9, cost_competitiveness: 5.5, overall_score: 8.8 },
    { supplier_id: 'SUP010', name: 'Alibaba Group', country: 'China', on_time_delivery_rate: 91.2, quality_score: 8.0, cost_competitiveness: 9.5, overall_score: 8.4 },
    { supplier_id: 'SUP011', name: 'Tata Industries', country: 'India', on_time_delivery_rate: 85.9, quality_score: 8.2, cost_competitiveness: 9.0, overall_score: 7.9 },
    { supplier_id: 'SUP012', name: 'Samsung Global', country: 'South Korea', on_time_delivery_rate: 98.8, quality_score: 9.6, cost_competitiveness: 7.2, overall_score: 9.0 },
    { supplier_id: 'SUP013', name: 'VinGroup', country: 'Vietnam', on_time_delivery_rate: 93.4, quality_score: 8.4, cost_competitiveness: 9.3, overall_score: 8.7 },
    { supplier_id: 'SUP014', name: 'Petronas Chemicals', country: 'Malaysia', on_time_delivery_rate: 96.0, quality_score: 8.8, cost_competitiveness: 8.6, overall_score: 8.8 },
    { supplier_id: 'SUP015', name: 'Toyota Auto Parts', country: 'Japan', on_time_delivery_rate: 99.5, quality_score: 9.7, cost_competitiveness: 7.0, overall_score: 9.1 },
    { supplier_id: 'SUP016', name: 'Huawei Tech', country: 'China', on_time_delivery_rate: 95.7, quality_score: 8.9, cost_competitiveness: 9.1, overall_score: 8.9 },
    { supplier_id: 'SUP017', name: 'Infosys Services', country: 'India', on_time_delivery_rate: 97.3, quality_score: 9.1, cost_competitiveness: 8.4, overall_score: 8.9 },
    { supplier_id: 'SUP018', name: 'LG Electronics', country: 'South Korea', on_time_delivery_rate: 98.2, quality_score: 9.4, cost_competitiveness: 7.9, overall_score: 8.9 },
    { supplier_id: 'SUP019', name: 'California Wines', country: 'USA', on_time_delivery_rate: 94.0, quality_score: 9.0, cost_competitiveness: 7.5, overall_score: 8.4 },
    { supplier_id: 'SUP020', name: 'Fashion Forward', country: 'USA', on_time_delivery_rate: 90.5, quality_score: 8.3, cost_competitiveness: 8.9, overall_score: 8.1 }
  ];
  res.json(scores);
});

// Démarrer le serveur
app.listen(PORT, () => {
  console.log(`WorldTrade API running on http://localhost:${PORT}`);
});