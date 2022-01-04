import DashboardLayout from "@/pages/Layout/DashboardLayout.vue";
import Dashboard from "@/pages/Dashboard.vue";
import Binance from "@/pages/Binance.vue";

const routes = [
  {
    path: "/",
    component: DashboardLayout,
    redirect: "/dashboard",
    children: [
      {
        path: "dashboard",
        name: "Dashboard",
        component: Dashboard,
      },
      {
        path: "binance",
        name: "Binance",
        component: Binance,
      },
      {
        path: "polychain",
        name: "Dashboard",
        component: Dashboard,
      }
    ],
  },
];

export default routes;
