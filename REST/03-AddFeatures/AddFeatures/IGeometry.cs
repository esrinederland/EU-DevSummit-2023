using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AddFeatures
{
    public interface IGeometry
    {
        SpatialReference SpatialReference { get; set; }

        string Type { get; }
    }
}
