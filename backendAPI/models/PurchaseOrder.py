from uuid import uuid4
from datetime import datetime
from typing import Optional, Any
from configs.extensions import dbModel

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID, JSON
from sqlalchemy import ForeignKey, Integer, Float, String, DateTime

class PurchaseOrders(dbModel):
    __tablename__ = "purchase_orders"

    po_number: Mapped[uuid4] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    vendor: Mapped[uuid4] = mapped_column(ForeignKey("vendors.vendor_code", ondelete="CASCADE"), nullable=False)
    order_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, default=datetime.now)
    delivery_date: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    items: Mapped[dict[str, Any]] = mapped_column(JSON, nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    status: Mapped[str]  = mapped_column(String(64), nullable=False, default='pending')
    quality_rating: Mapped[Optional[float]]  = mapped_column(Float, nullable=True)
    issue_date: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    acknowledgment_date: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)

    def __init__(self, **kwargs):
        super(PurchaseOrders, self).__init__(**kwargs)

    def __repr__(self):
        return f'<PO {self.po_number.hex}[{self.order_date}]>'
    
    # def db_write(self):
    #     db.session.add(self)
        # db.session.commit()